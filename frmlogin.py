import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from frmuser import User
from frmdashboard import Dashboard
import bll.usuarios as user
from MenuUsuario import MenUsuario

class Login(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Identificación") 
        #setting window size
        width=405
        height=140
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        
        GLineEdit_511=tk.Entry(self, name="txtUsuario")
        GLineEdit_511["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_511["font"] = ft
        GLineEdit_511["fg"] = "#333333"
        GLineEdit_511["justify"] = "left"
        GLineEdit_511["text"] = "acobos"
        GLineEdit_511.place(x=110,y=10,width=280,height=25)

        GLineEdit_723=tk.Entry(self, name ="txtContrasenia", show="*")
        GLineEdit_723["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_723["font"] = ft
        GLineEdit_723["fg"] = "#333333"
        GLineEdit_723["justify"] = "left"
        GLineEdit_723["text"] = "123456"
        GLineEdit_723.place(x=110,y=50,width=280,height=25)

        GLabel_787=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_787["font"] = ft
        GLabel_787["fg"] = "#333333"
        GLabel_787["justify"] = "center"
        GLabel_787["text"] = "Usuario:"
        GLabel_787.place(x=40,y=10,width=70,height=25)

        GLabel_267=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_267["font"] = ft
        GLabel_267["fg"] = "#333333"
        GLabel_267["justify"] = "center"
        GLabel_267["text"] = "Contraseña:"
        GLabel_267.place(x=30,y=50,width=70,height=25)
        

        GButton_962=tk.Button(self)
        GButton_962["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_962["font"] = ft
        GButton_962["fg"] = "#000000"
        GButton_962["justify"] = "center"
        GButton_962["text"] = "Aceptar"
        GButton_962.place(x=230,y=100,width=70,height=25)
        GButton_962["command"] = self.iniciar_sesion

        GButton_290=tk.Button(self)
        GButton_290["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_290["font"] = ft
        GButton_290["fg"] = "#000000"
        GButton_290["justify"] = "center"
        GButton_290["text"] = "Cancelar"
        GButton_290.place(x=320,y=100,width=70,height=25)
        GButton_290["command"] = self.cerrar

        GButton_722=tk.Button(self)
        GButton_722["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_722["font"] = ft
        GButton_722["fg"] = "#000000"
        GButton_722["justify"] = "center"
        GButton_722["text"] = "Usuario Nuevo"
        GButton_722.place(x=30,y=100,width=100,height=25)
        GButton_722["command"] = self.abrir_user

    def iniciar_sesion(self):
        try:
            txtUsuario = self.nametowidget("txtUsuario")
            usuario = txtUsuario.get()            

            txtContrasenia = self.nametowidget("txtContrasenia")
            contrasenia = txtContrasenia.get()

            if usuario != "":
                if user.validar(usuario, contrasenia):
                    usuario = user.obtener_nombre_usuario(usuario)
                    if usuario is not None:
                        if usuario[8] == "Administrador":
                            Dashboard(self.master)
                            self.destroy()
                        elif usuario[8] == "Cliente":
                             MenUsuario(self.master)
                    
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

    def cerrar(self):
        self.destroy()


    def abrir_user(self):
        User(self.master)


