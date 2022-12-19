import tkinter as tk
import tkinter.font as tkFont
from frmusers import Users
from frmsalas import Salas
from frmpeliculas import Peliculas
from frmfunciones import Funciones

class Dashboard(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master        
        self.title("Menú Principal")        
        width=548
        height=407
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_245=tk.Button(self)
        GButton_245["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_245["font"] = ft
        GButton_245["fg"] = "#000000"
        GButton_245["justify"] = "center"
        GButton_245["text"] = "Usuarios"
        GButton_245.place(x=10,y=40,width=165,height=45)
        GButton_245["command"] = self.abrir_usuarios

        Button_peliculas=tk.Button(self)
        Button_peliculas["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Button_peliculas["font"] = ft
        Button_peliculas["fg"] = "#000000"
        Button_peliculas["justify"] = "center"
        Button_peliculas["text"] = "Peliculas"
        Button_peliculas.place(x=10,y=150,width=165,height=45)
        Button_peliculas["command"] = self.abrir_peliculas

        Button_funciones=tk.Button(self)
        Button_funciones["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Button_funciones["font"] = ft
        Button_funciones["fg"] = "#000000"
        Button_funciones["justify"] = "center"
        Button_funciones["text"] = "Funciones"
        Button_funciones.place(x=190,y=150,width=165,height=45)
        Button_funciones["command"] = self.abrir_funciones

        GLabel_996=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_996["font"] = ft
        GLabel_996["fg"] = "#333333"
        GLabel_996["justify"] = "left"
        GLabel_996["text"] = "Administración:"
        GLabel_996.place(x=10,y=10,width=120,height=30)

        GButton_196=tk.Button(self)
        GButton_196["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_196["font"] = ft
        GButton_196["fg"] = "#000000"
        GButton_196["justify"] = "center"
        GButton_196["text"] = "Salas"
        GButton_196.place(x=190,y=40,width=165,height=45)
        GButton_196["command"] = self.abrir_salas

        GButton_430=tk.Button(self)
        GButton_430["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "Descuentos"
        GButton_430.place(x=370,y=40,width=165,height=45)
        GButton_430["command"] = self.abrir_descuentos

    def abrir_usuarios(self):
        Users(self)

    def abrir_salas(self):
        Salas(self)

    def abrir_peliculas(self):
        Peliculas(self)

    def abrir_funciones(self):
        Funciones(self)

    def abrir_descuentos(self):
        print("descuentos")