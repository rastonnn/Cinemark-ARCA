import tkinter as tk
import tkinter.font as tkFont
from frmlogin import Login
from dal.db import Db

class App:
    def __init__(self, root):
        self.root = root
        #setting title
        root.title("Proyecto Cinemar - Grupo ARCA")
        #setting window size
        width=580
        height=111
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_71=tk.Button(root)
        GButton_71["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "Cinermar"
        GButton_71.place(x=50,y=30,width=480,height=45)
        GButton_71["command"] = self.abrir_login

    def abrir_login(self):
        Login(self.root)
        #print("hola mundo")

if __name__ == "__main__":
    Db.crear_tablas()
    Db.poblar_tablas()
    root = tk.Tk()
    root.iconbitmap(default=f"cinemar.ico")
    app = App(root)
    root.mainloop()
