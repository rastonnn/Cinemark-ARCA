from tkinter import *
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter.messagebox as tkMsgBox
import bll.peliculas as peli
from RegistroPeli import Peli

class Registro(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.select_id = -1 
        self.title("Formulario peliculas")
        #setting window size
        width=773
        height=443
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_74=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_74["font"] = ft
        GLabel_74["fg"] = "#333333"
        GLabel_74["justify"] = "center"
        GLabel_74["text"] = "Peliculas:"
        GLabel_74.place(x=10,y=30,width=133,height=30)

        
        tv = ttk.Treeview(self, columns=("nombrepeli", "genero", "idioma", "clasificacion"," calidad"), name="tvPeliculas")
        tv.column("#0", width=78)
        tv.column("nombrepeli", width=100, anchor=CENTER)
        tv.column("genero", width=150, anchor=CENTER)
        tv.column("idioma", width=150, anchor=CENTER)
        tv.column("clasificacion", width=150, anchor=CENTER)
        tv.column("calidad", width=120, anchor=CENTER)

        tv.heading("#0", text="Id", anchor=CENTER)
        tv.heading("nombrepeli", text="Nombrepeli", anchor=CENTER)
        tv.heading("genero", text="Genero", anchor=CENTER)
        tv.heading("idioma", text="Idioma", anchor=CENTER)
        tv.heading("clasificacion", text="Clasificacion", anchor=CENTER)
        tv.heading("calidad", text="Calidad", anchor=CENTER)
        tv.bind("<<TreeviewSelect>>", self.obtener_fila)
        tv.place(x=10,y=60,width=750,height=300)          
        
        self.refrescar()

        GButton_656= Button(self)
        GButton_656["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_656["font"] = ft
        GButton_656["fg"] = "#000000"
        GButton_656["justify"] = "center"
        GButton_656["text"] = "Agregar"
        GButton_656.place(x=290,y=30,width=70,height=25)
        GButton_656["command"] = self.agregar

        GButton_719= Button(self)
        GButton_719["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_719["font"] = ft
        GButton_719["fg"] = "#000000"
        GButton_719["justify"] = "center"
        GButton_719["text"] = "Editar"
        GButton_719.place(x=380,y=30,width=70,height=25)
        GButton_719["command"] = self.editar

        GButton_932= Button(self)
        GButton_932["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_932["font"] = ft
        GButton_932["fg"] = "#000000"
        GButton_932["justify"] = "center"
        GButton_932["text"] = "Eliminar"
        GButton_932.place(x=470,y=30,width=70,height=25)
        GButton_932["command"] = self.eliminar

        
    def obtener_fila(self, event):
        tvPeliculas = self.nametowidget("tvPeliculas")
        current_item = tvPeliculas.focus()
        if current_item:
            data = tvPeliculas.item(current_item)
            self.select_id = int(data["text"])
        else:
            self.select_id = -1
        
    def agregar(self):
        Peli(self, True)

    def editar(self): 
        Peli(self, True, self.select_id)

    def eliminar(self):
        answer =  tkMsgBox.askokcancel(self.master.master.title(), "¿Está seguro de eliminar este registro?")   
        if answer:
            peli.eliminar(self.select_id)
            self.refrescar()

    def refrescar(self):        
        tvPeliculas = self.nametowidget("tvPeliculas")
        for record in tvPeliculas.get_children():
            tvPeliculas.delete(record)
        peliculas = peli.listar()
        for pelicula in peliculas:
            tvPeliculas.insert("", END, text=pelicula[0], values=(pelicula[1], pelicula[2], pelicula[3], pelicula[4], pelicula[5]))
