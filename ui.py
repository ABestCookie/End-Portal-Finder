from tkinter import Tk, Label, ttk, messagebox, Menu
from ttkbootstrap import Style

import os, sys, webbrowser
from sympy import symbols, Eq, solve

class app:
    
    def search_tool(self, apx, apy, bpx, bpy, cpx, cpy, dpx, dpy):
        global x, y, solution, x_value, z_value

        x, y = symbols('x y')
        ap=[float(apx), float(apy)]
        bp=[float(bpx), float(bpy)]
        #設二元一次式第一式為ax+by=c
        a=(ap[1]-bp[1])
        b=(ap[0]- bp[0])
        c=((ap[0]*a)+(ap[1]*b))
        eq1 = Eq(a*x + b*y, c)

        cp=[float(cpx), float(cpy)]
        dp=[float(dpx), float(dpy)]
        #設二元一次式第二式為dx+ey=f
        d=(cp[1]-dp[1])
        e=(cp[0]- dp[0])
        f=((cp[0]*d)+(cp[1]*e))
        eq2 = Eq(d*x + e*y, f)

        solution = solve((eq1, eq2), (x, y))

    
        x_value = solution[x].evalf()
        z_value = solution[y].evalf()

    def get_x_value(self):
        return x_value
    
    def get_z_value(self):
        return z_value



def calc():
    pop = app()
    try:
        pop.search_tool(apx=e1.get(), apy=e2.get(), bpx=e3.get(), bpy=e4.get(), 
                        cpx=e5.get(), cpy=e6.get(), dpx=e7.get(), dpy=e8.get())
        
        a1 = Label(main, text=pop.get_x_value(), font=("Times New Roman", 15))
        a1.grid(row=10, column=1)
        a2 = Label(main, text=pop.get_z_value(), font=("Times New Roman", 15))
        a2.grid(row=11, column=1)
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")


def helper():
    try:
        website_path="index.html"
        if os.path.join(os.path.abspath(os.path.dirname(__file__)), website_path):
            webbrowser.open(website_path)
        else:
            messagebox.showerror("Error", f"Failed to open help: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open help: {e}")

def disable_close():
    sys.exit(0)
    

def application():
    global main, e1, e2, e3, e4, e5, e6, e7, e8

    main = Tk()
    style = Style(theme='solar')
    TOP6 = style.master

    main.title("終界祭壇尋找器 by ABestCookie")
    main.geometry("380x450")
    main.resizable(False, False)
    main.protocol("WM_DELETE_WINDOW", disable_close)

    icon_path = "icon.ico"
    if os.path.join(os.path.abspath(os.path.dirname(__file__)), icon_path):
        main.iconbitmap(icon_path)
    else:
        print("Warning: Icon file not found")


    menu = Menu(main)
    menu.add_command(label="教學", command=helper)
    menu.add_command(label="退出", command=(lambda: sys.exit(0)))
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
    application()
