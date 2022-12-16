import tkinter as tk
import tkinter.font as tkFont
from login import Login
from dal.db import Db

class App:
    def __init__(self, root,title):
        self.root = root
        #setting title
        root.title(title)
        #setting window size
        width=589
        height=148
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_697=tk.Button(root)
        GButton_697["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=14)
        GButton_697["font"] = ft
        GButton_697["fg"] = "#000000"
        GButton_697["justify"] = "center"
        GButton_697["text"] = "" + title
        GButton_697.place(x=110,y=30,width=348,height=30)
        GButton_697["command"] = self.GButton_697_command

    def abrir_login(self):
        Login(self.root)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
