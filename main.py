import random
import tkinter as tk
import subprocess
import threading
import time
import json

# 定義定時彈出的間隔時間（秒）
POPUP_INTERVAL_SECONDS = 60 # 這裡設置為30秒，您可以根據需要修改

def get_random_word_from_file(filename="words.json"):
    """從 JSON 檔案中讀取單詞，並隨機返回一個。"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list) and data:
                return random.choice(data)
    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {filename}")
    except json.JSONDecodeError:
        print(f"錯誤：檔案 {filename} 的 JSON 格式不正確")
    except Exception as e:
        print(f"讀取檔案時發生錯誤：{e}")
    
    return None

def speak_text(text_to_speak):
    """調用 espeak 命令行工具來朗讀單詞或例句。"""
    try:
        # 使用 -s 參數調整語速，-v 參數指定英音
        subprocess.run(["espeak", "-s", "150", "-v", "en-uk", text_to_speak], check=True)
    except FileNotFoundError:
        print("錯誤：未找到 espeak。請安裝 espeak 以啟用發音功能。")
    except Exception as e:
        print(f"發音時發生錯誤：{e}")

def speak_sequence(word, example, window):
    """
    按順序朗讀單詞和例句，並控制播放次數和間隔。
    """
    # 延遲3秒後開始播放
    time.sleep(3)
    
    # 預熱 espeak，避免第一個音節丟失
    try:
        subprocess.run(["espeak", "-s", "150", "-v", "en-uk", "."], check=True)
        # 在預熱後，再等待1秒，以確保espeak完全就緒
        time.sleep(1)
    except Exception as e:
        print(f"Espeak 預熱時發生錯誤：{e}")

    for _ in range(3): # 共重複三次
        # 朗讀單詞
        speak_text(word)
        time.sleep(3)
        # 朗讀例句
        speak_text(example)
        # 每次播放後等待5秒
        time.sleep(5)
    
    # 播放完畢，再等待3秒後關閉對話框
    time.sleep(3)
    window.destroy()

def create_and_schedule_popup(main_window):
    """創建一個新的視窗，並設置自動播放、關閉和下一次彈出。"""
    word_data = get_random_word_from_file()

    if not word_data:
        main_window.after(POPUP_INTERVAL_SECONDS * 1000, lambda: create_and_schedule_popup(main_window))
        return

    window = tk.Toplevel(main_window)
    window.title("Daily Brit")
    window.geometry("300x250")

    # 創建並顯示單詞
    word_label = tk.Label(window, text=word_data['word'], font=("Helvetica", 24, "bold"))
    word_label.pack(pady=(10, 5))

    # 創建並顯示音標
    pronunciation_label = tk.Label(window, text=word_data['accent'], font=("Helvetica", 16))
    pronunciation_label.pack(pady=(0, 5))

    # 添加中文解釋
    tw_label = tk.Label(window, text=f"中文：{word_data['tw']}", font=("Helvetica", 12))
    tw_label.pack()

    # 添加例句
    example_label = tk.Label(window, text=f"例句：{word_data['example']}", font=("Helvetica", 12), wraplength=280, justify="left")
    example_label.pack()

    # 添加例句翻譯
    tw_ex_label = tk.Label(window, text=f"翻譯：{word_data['tw_ex']}", font=("Helvetica", 12), wraplength=280, justify="left")
    tw_ex_label.pack()

    # 安排下一次彈出
    main_window.after(POPUP_INTERVAL_SECONDS * 1000, lambda: create_and_schedule_popup(main_window))

    # 使用一個新的執行緒來進行發音和自動關閉，以避免阻塞GUI
    threading.Thread(target=speak_sequence, args=(word_data['word'], word_data['example'], window)).start()

if __name__ == "__main__":
    print("Daily Brit 助手已在後台運行...")
    print(f"每隔 {POPUP_INTERVAL_SECONDS} 秒會彈出一個新的單詞視窗。")
    print("要停止，請按 Ctrl+C。")

    # 創建一個主視窗來處理事件循環，但我們將它隱藏
    root = tk.Tk()
    root.withdraw()
    
    # 安排第一次彈出，以便在啟動時就顯示第一個單詞
    root.after(1000, lambda: create_and_schedule_popup(root))
    
    # 運行主事件循環
    root.mainloop()