from tkinter import Tk, Label, PhotoImage, ttk, messagebox, Menu
from ttkbootstrap import Style
from main import app
import os
#給chatgtp修過之前


pop=app()
def calc():
    try:
        pop.search_tool(apx=e1.get(), apy=e2.get(), bpx=e3.get(), bpy=e4.get(), 
                cpx=e5.get(), cpy=e6.get(), dpx=e7.get(), dpy=e8.get())
        
        a1=Label(main, text=pop.get_x_value(), font=("Times New Roman", 15))
        a1.grid(row=10, column=1)
        a2=Label(main, text=pop.get_z_value(), font=("Times New Roman", 15))
        a2.grid(row=11, column=1)
    except Exception as e:
        messagebox.showerror("error",f"預期外的錯誤 {e}")
        pass

def exit_app():
    main.destroy()

def help():
    os.system("htmlui.py")


def __main__():
    global main, e1, e2, e3, e4, e5, e6, e7, e8, style, TOP6

    main=Tk()

    style = Style(theme='solar')
#想要切换主题，修改theme值即可，有以下这么多的主题，自己尝试吧：['vista', 'classic', 'cyborg', 'journal', 'darkly', 'flatly', 'clam', 'alt', 'solar', 'minty', 'litera', 'united', 'xpnative', 'pulse', 'cosmo', 'lumen', 'yeti', 'superhero', 'winnative', 'sandstone', 'default']
    TOP6 = style.master
#这两行代码在自己原基础的代码上加入即可，放在代码的最开端部分，也就是在窗口创建代码之前

    main.title("終界祭壇尋找器 by ABestCookie")
    main.geometry("380x450")
    main.resizable(False, False)
    icon=os.path.join("", "icon.ico")
    main.iconbitmap(icon)

    menu=Menu(main)
    menu.add_command(label="教學", command=help)
    menu.add_command(label="退出", command=exit_app)

    main.config(menu=menu)

    w=Label(main, text="第一點x座標:", font=("Times New Roman", 15))
    w.grid(row=0, column=0)
    w=Label(main, text="第一點z座標:", font=("Times New Roman", 15))
    w.grid(row=1, column=0)
    w=Label(main, text="第二點x座標:", font=("Times New Roman", 15))
    w.grid(row=2, column=0)
    w=Label(main, text="第二點z座標:", font=("Times New Roman", 15))
    w.grid(row=3, column=0)

    e1=ttk.Entry(main, width=25)
    e1.grid(row=0, column=1)
    e2=ttk.Entry(main, width=25)
    e2.grid(row=1, column=1)
    e3=ttk.Entry(main, width=25)
    e3.grid(row=2, column=1)
    e4=ttk.Entry(main, width=25)
    e4.grid(row=3, column=1)

    w=Label(main, text="第三點x座標:", font=("Times New Roman", 15))
    w.grid(row=4, column=0)
    w=Label(main, text="第三點z座標:", font=("Times New Roman", 15))
    w.grid(row=5, column=0)
    w=Label(main, text="第四點x座標:", font=("Times New Roman", 15))
    w.grid(row=6, column=0)
    w=Label(main, text="第四點z座標:", font=("Times New Roman", 15))
    w.grid(row=7, column=0)

    e5=ttk.Entry(main, width=25)
    e5.grid(row=4, column=1)
    e6=ttk.Entry(main, width=25)
    e6.grid(row=5, column=1)
    e7=ttk.Entry(main, width=25)
    e7.grid(row=6, column=1)
    e8=ttk.Entry(main, width=25)
    e8.grid(row=7, column=1)

    b1=ttk.Button(main, text="計算座標", command=calc)
    b1.grid(row=8, column=1)

    s=Label(main, text="", font=("Times New Roman", 15))
    s.grid(row=9, column=0)

    w=Label(main, text="x座標(大約) = ", font=("Times New Roman", 15))
    w.grid(row=10, column=0)
    w=Label(main, text="z座標(大約) = ", font=("Times New Roman", 15))
    w.grid(row=11, column=0)

    main.mainloop()


__main__()