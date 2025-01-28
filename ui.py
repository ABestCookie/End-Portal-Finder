from tkinter import Tk, Label, PhotoImage, ttk, messagebox, Menu
from ttkbootstrap import Style
from main import app
import os, eel, threading


pop = app()

def calc():
    try:
        pop.search_tool(apx=e1.get(), apy=e2.get(), bpx=e3.get(), bpy=e4.get(), 
                        cpx=e5.get(), cpy=e6.get(), dpx=e7.get(), dpy=e8.get())
        
        a1 = Label(main, text=pop.get_x_value(), font=("Times New Roman", 15))
        a1.grid(row=10, column=1)
        a2 = Label(main, text=pop.get_z_value(), font=("Times New Roman", 15))
        a2.grid(row=11, column=1)
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")

def exit_app():
    main.destroy()

@eel.expose
def help():
    # 使用執行緒來運行 eel，避免阻塞主線程
    eel.init('doc')
    threading.Thread(target=eel.start, args=("README.md.html",), kwargs={'size': (600, 800), 'port': 0}, daemon=True).start()
        

def __main():
    global main, e1, e2, e3, e4, e5, e6, e7, e8

    main = Tk()
    style = Style(theme='solar')
    TOP6 = style.master

    main.title("終界祭壇尋找器 by ABestCookie")
    main.geometry("380x450")
    main.resizable(False, False)

    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    if os.path.exists(icon_path):
        main.iconbitmap(icon_path)
    else:
        print("Warning: Icon file not found")

    menu = Menu(main)
    menu.add_command(label="教學", command=help)
    menu.add_command(label="退出", command=exit_app)
    main.config(menu=menu)

    labels = ["第一點x座標:", "第一點z座標:", "第二點x座標:", "第二點z座標:",
              "第三點x座標:", "第三點z座標:", "第四點x座標:", "第四點z座標:"]
    entries = []

    for i, label in enumerate(labels):
        Label(main, text=label, font=("Times New Roman", 15)).grid(row=i, column=0)
        entry = ttk.Entry(main, width=25)
        entry.grid(row=i, column=1)
        entries.append(entry)

    global e1, e2, e3, e4, e5, e6, e7, e8
    e1, e2, e3, e4, e5, e6, e7, e8 = entries

    ttk.Button(main, text="計算座標", command=calc).grid(row=8, column=1)
    Label(main, text="x座標(大約) = ", font=("Times New Roman", 15)).grid(row=10, column=0)
    Label(main, text="z座標(大約) = ", font=("Times New Roman", 15)).grid(row=11, column=0)

    main.mainloop()

if __name__ == "__main__":
    __main()
