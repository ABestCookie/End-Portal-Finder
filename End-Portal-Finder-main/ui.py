from tkinter import Tk, Label, PhotoImage, ttk, messagebox, Menu
import eel.chrome
from ttkbootstrap import Style
from main import app
import os, eel, sys, subprocess, threading
import http.server
import socketserver



pop = app()

def server():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

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




def help():
    threading.Thread(target=server, args=(), kwargs={}, daemon=True).start()
    threading.Thread(target=subprocess.run, args=(["chrome_app.bat"]), kwargs={}, daemon=True).start()

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
    menu.add_command(label="退出", command=sys.exit)
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
