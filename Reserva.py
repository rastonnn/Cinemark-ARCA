import tkinter as tk
import tkinter.font as tkFont

class Reservas(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)        
        self.master = master
        self.title("Reserva")
        #setting window size
        width=644
        height=297
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_131=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_131["font"] = ft
        GLabel_131["fg"] = "#333333"
        GLabel_131["justify"] = "right"
        GLabel_131["text"] = "Pelicula:"
        GLabel_131.place(x=40,y=40,width=114,height=30)

        GListBox_202=tk.Listbox(self)
        GListBox_202["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_202["font"] = ft
        GListBox_202["fg"] = "#333333"
        GListBox_202["justify"] = "center"
        GListBox_202.place(x=200,y=40,width=314,height=30)

        GLabel_43=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_43["font"] = ft
        GLabel_43["fg"] = "#333333"
        GLabel_43["justify"] = "right"
        GLabel_43["text"] = "DIa Funcion:"
        GLabel_43.place(x=40,y=90,width=116,height=34)

        GListBox_787=tk.Listbox(self)
        GListBox_787["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_787["font"] = ft
        GListBox_787["fg"] = "#333333"
        GListBox_787["justify"] = "center"
        GListBox_787.place(x=200,y=90,width=315,height=32)

        GLabel_643=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_643["font"] = ft
        GLabel_643["fg"] = "#333333"
        GLabel_643["justify"] = "right"
        GLabel_643["text"] = "horario Funcion:"
        GLabel_643.place(x=40,y=140,width=126,height=30)

        GListBox_566=tk.Listbox(self)
        GListBox_566["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_566["font"] = ft
        GListBox_566["fg"] = "#333333"
        GListBox_566["justify"] = "center"
        GListBox_566.place(x=200,y=140,width=313,height=30)

        GButton_893=tk.Button(self)
        GButton_893["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_893["font"] = ft
        GButton_893["fg"] = "#000000"
        GButton_893["justify"] = "center"
        GButton_893["text"] = "cancelar"
        GButton_893.place(x=420,y=190,width=98,height=30)
        GButton_893["command"] = self.cancelar

        GButton_779=tk.Button(self)
        GButton_779["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_779["font"] = ft
        GButton_779["fg"] = "#000000"
        GButton_779["justify"] = "center"
        GButton_779["text"] = "aceptar"
        GButton_779.place(x=310,y=190,width=102,height=30)
        GButton_779["command"] = self.GButton_779_command

    def cancelar(self):
        self.destroy()


    def GButton_779_command(self):
        print("command")

