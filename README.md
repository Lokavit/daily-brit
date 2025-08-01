# daily-brit

Liunx tool

Python + Tkinter。
「英音學習助手」可以分解為以下幾個核心功能模組：

單詞庫管理：

您可以用一個文字檔案或一個 Python 字典來存放單詞和它們的英式音標。

學習內容： 學習如何讀取、解析和隨機選擇檔案中的內容。

圖形用戶界面（GUI）創建：

使用 Tkinter 來創建一個小視窗。

視窗內容： 包含一個顯示單詞的標籤、一個顯示音標的標籤，以及一個「發音」按鈕。

學習內容： 學習 Tkinter 的基本組件（Label、Button）、如何佈局和處理用戶點擊事件。

文本轉語音（TTS）功能：

您可以調用 Linux 系統中的文本轉語音工具來朗讀單詞。最常見的命令行工具是 espeak 或 Festival。

學習內容： 學習如何使用 Python 的 subprocess 模組來調用系統命令，並傳遞參數給它。

定時任務：

使用 Python 的 threading 或 time 模組來實現定時功能。

學習內容： 學習如何讓程式每隔一段時間（例如一小時）自動執行一次任務，即彈出視窗並顯示新單詞。

## 安裝 python 環境

```bash
python3 --version # 檢查 Python 環境
python3 -m pip --version # 確保安裝了 pip
sudo apt install python3-pip # 如果報錯，則需要安裝它：
sudo apt install python3-tk # 安裝 Tkinter（圖形界面庫）
sudo apt install espeak # 安裝 TTS 命令行工具
```
