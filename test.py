import tkinter as tk

def show_message():
    window = tk.Tk()
    window.title("Hello World")
    label = tk.Label(window, text="Python環境測試成功!")
    label.pack(padx=20, pady=20)
    window.mainloop()

if __name__ == "__main__":
    print("正在運行Python環境測試...")
    show_message()