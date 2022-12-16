from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.usuarios as user
import bll.roles as rol
from datetime import date

class user(Toplevel):
    def __init__(self, master = None, isAdmin = False, user_id = None):
        super(). __init__(master)
        self.master = master
        self.user_id = user_id
        #setting title
        self.title("Registro de cuenta")
        #setting window size
        width=600
        height=500
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_738= Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_738["font"] = ft
        GLabel_738["fg"] = "#333333"
        GLabel_738["justify"] = "right"
        GLabel_738["text"] = "Apellido:"
        GLabel_738.place(x=40,y=10,width=121,height=30)

        GLineEdit_396= Entry(self, name="txtApellido")
        GLineEdit_396["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_396["font"] = ft
        GLineEdit_396["fg"] = "#333333"
        GLineEdit_396["justify"] = "left"
        GLineEdit_396["text"] = ""
        GLineEdit_396.place(x=190,y=10,width=353,height=30)

        GLabel_102= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_102["font"] = ft
        GLabel_102["fg"] = "#333333"
        GLabel_102["justify"] = "right"
        GLabel_102["text"] = "Nombre:"
        GLabel_102.place(x=40,y=50,width=121,height=30)

        GLineEdit_179= Entry(self, name="txtNombre")
        GLineEdit_179["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_179["font"] = ft
        GLineEdit_179["fg"] = "#333333"
        GLineEdit_179["justify"] = "left"
        GLineEdit_179["text"] = ""
        GLineEdit_179.place(x=190,y=50,width=352,height=30)

        GLabel_551= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#333333"
        GLabel_551["justify"] = "right"
        GLabel_551["text"] = "Fecha_Nac:"
        GLabel_551.place(x=40,y=90,width=123,height=30)

        GLineEdit_411= Entry(self, name= "txtFecha_Nac")
        GLineEdit_411["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_411["font"] = ft
        GLineEdit_411["fg"] = "#333333"
        GLineEdit_411["justify"] = "left"
        GLineEdit_411["text"] = ""
        GLineEdit_411.place(x=190,y=90,width=352,height=30)

        GLabel_584= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_584["font"] = ft
        GLabel_584["fg"] = "#333333"
        GLabel_584["justify"] = "right"
        GLabel_584["text"] = "Dni:"
        GLabel_584.place(x=40,y=130,width=127,height=30)

        GLineEdit_187= Entry(self, name= "txtDni")
        GLineEdit_187["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_187["font"] = ft
        GLineEdit_187["fg"] = "#333333"
        GLineEdit_187["justify"] = "left"
        GLineEdit_187["text"] = ""
        GLineEdit_187.place(x=190,y=130,width=352,height=30)

        GLabel_181= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_181["font"] = ft
        GLabel_181["fg"] = "#333333"
        GLabel_181["justify"] = "right"
        GLabel_181["text"] = "E-mail:"
        GLabel_181.place(x=40,y=170,width=124,height=30)

        GLineEdit_623= Entry(self, name ="txtE-mail")
        GLineEdit_623["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_623["font"] = ft
        GLineEdit_623["fg"] = "#333333"
        GLineEdit_623["justify"] = "left"
        GLineEdit_623["text"] = ""
        GLineEdit_623.place(x=190,y=170,width=349,height=30)

        GLabel_918= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_918["font"] = ft
        GLabel_918["fg"] = "#333333"
        GLabel_918["justify"] = "right"
        GLabel_918["text"] = "Usuario:"
        GLabel_918.place(x=40,y=210,width=124,height=30)

        GLineEdit_62= Entry(self, name= "txtUsuario")
        GLineEdit_62["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_62["font"] = ft
        GLineEdit_62["fg"] = "#333333"
        GLineEdit_62["justify"] = "left"
        GLineEdit_62["text"] = ""
        GLineEdit_62.place(x=190,y=210,width=352,height=30)

        GLabel_800= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_800["font"] = ft
        GLabel_800["fg"] = "#333333"
        GLabel_800["justify"] = "right"
        GLabel_800["text"] = "Contraseña:"
        GLabel_800.place(x=40,y=250,width=128,height=30)

        GLineEdit_367= Entry(self, name = "txtContraseña")
        GLineEdit_367["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_367["font"] = ft
        GLineEdit_367["fg"] = "#333333"
        GLineEdit_367["justify"] = "left"
        GLineEdit_367["text"] = ""
        GLineEdit_367.place(x=190,y=250,width=350,height=30)

        GLabel_780= Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_780["font"] = ft
        GLabel_780["fg"] = "#333333"
        GLabel_780["justify"] = "right"
        GLabel_780["text"] = "Confirmar Contraseña"
        GLabel_780.place(x=40,y=290,width=129,height=30)

        GLineEdit_803= Entry(self, name = "txtConfirmacion")
        GLineEdit_803["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_803["font"] = ft
        GLineEdit_803["fg"] = "#333333"
        GLineEdit_803["justify"] = "left"
        GLineEdit_803["text"] = ""
        GLineEdit_803.place(x=190,y=290,width=351,height=30)

        GLabel_88=Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_88["font"] = ft
        GLabel_88["fg"] = "#333333"
        GLabel_88["justify"] = "center"
        GLabel_88["text"] = "Rol:"
        GLabel_88.place(x=90,y=340,width=81,height=30)

        GButton_821=tk.Button(root)
        GButton_821["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_821["font"] = ft
        GButton_821["fg"] = "#000000"
        GButton_821["justify"] = "center"
        GButton_821["text"] = "Aceptar"
        GButton_821.place(x=310,y=350,width=108,height=30)
        GButton_821["command"] = self.GButton_821_command

        GButton_602=tk.Button(root)
        GButton_602["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_602["font"] = ft
        GButton_602["fg"] = "#000000"
        GButton_602["justify"] = "center"
        GButton_602["text"] = "Cancelar"
        GButton_602.place(x=430,y=350,width=110,height=30)
        GButton_602["command"] = self.GButton_602_command

    def GButton_821_command(self):
        print("command")


    def GButton_602_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
