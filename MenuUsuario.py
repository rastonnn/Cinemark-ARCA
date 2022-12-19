import tkinter as tk
import tkinter.font as tkFont
from Reserva import Reservas

class MenUsuario(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("Menu Usuario")
        #setting window size
        width=621
        height=287
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GButton_323=tk.Button(self)
        GButton_323["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_323["font"] = ft
        GButton_323["fg"] = "#000000"
        GButton_323["justify"] = "center"
        GButton_323["text"] = "Reserva"
        GButton_323.place(x=50,y=30,width=172,height=69)
        GButton_323["command"] = self.abrir_Reserva

        GButton_962=tk.Button(self)
        GButton_962["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_962["font"] = ft
        GButton_962["fg"] = "#000000"
        GButton_962["justify"] = "center"
        GButton_962["text"] = "Cartelera"
        GButton_962.place(x=320,y=30,width=171,height=69)
        GButton_962["command"] = self.abrir_Cartelera

        GButton_35=tk.Button(self)
        GButton_35["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_35["font"] = ft
        GButton_35["fg"] = "#000000"
        GButton_35["justify"] = "center"
        GButton_35["text"] = "Cancelar Reserva"
        GButton_35.place(x=190,y=130,width=171,height=70)
        GButton_35["command"] = self.abrir_Cancelar_Reserva

    def abrir_Reserva(self):
        Reservas(self)

    def abrir_Cartelera(self):
        print("abrir cartelera")

    def abrir_Cancelar_Reserva(self):
        print("Cancelar_Reserva")