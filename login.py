import tkinter as tk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
from frmcuentas import User
from frmdashboard import Dashboard
import bll.usuarios as user


class Login(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.title("login")
        width=585
        height=326
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLineEdit_957=tk.Entry(self, name= "txtUsuario")
        GLineEdit_957["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_957["font"] = ft
        GLineEdit_957["fg"] = "#333333"
        GLineEdit_957["justify"] = "left"
        GLineEdit_957["text"] = ""
        GLineEdit_957.place(x=140,y=40,width=357,height=32)

        GLineEdit_834=tk.Entry(self, name= "txtContraseña", show= ":)")
        GLineEdit_834["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_834["font"] = ft
        GLineEdit_834["fg"] = "#333333"
        GLineEdit_834["justify"] = "left"
        GLineEdit_834["text"] = ""
        GLineEdit_834.place(x=140,y=90,width=356,height=30)

        GLabel_691=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_691["font"] = ft
        GLabel_691["fg"] = "#333333"
        GLabel_691["justify"] = "right"
        GLabel_691["text"] = "Usuario:"
        GLabel_691.place(x=30,y=50,width=70,height=25)

        GLabel_890=tk.Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_890["font"] = ft
        GLabel_890["fg"] = "#333333"
        GLabel_890["justify"] = "center"
        GLabel_890["text"] = "Contraseña:"
        GLabel_890.place(x=40,y=100,width=70,height=25)

        

        

        GButton_570=tk.Button(self)
        GButton_570["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_570["font"] = ft
        GButton_570["fg"] = "#000000"
        GButton_570["justify"] = "center"
        GButton_570["text"] = "Aceptar"
        GButton_570.place(x=290,y=140,width=102,height=30)
        GButton_570["command"] = self.iniciar_sesion

        GButton_842=tk.Button(self)
        GButton_842["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_842["font"] = ft
        GButton_842["fg"] = "#000000"
        GButton_842["justify"] = "center"
        GButton_842["text"] = "Cancelar"
        GButton_842.place(x=400,y=140,width=102,height=30)
        GButton_842["command"] = self.cancelar

        GButton_130=tk.Button(self)
        GButton_130["bg"] = "#f0f0f0"
        GButton_130["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GButton_130["font"] = ft
        GButton_130["fg"] = "#000000"
        GButton_130["justify"] = "center"
        GButton_130["text"] = "Crear Cuenta"
        GButton_130.place(x=30,y=140,width=125,height=30)
        GButton_130["command"] = self.abrir_user

        GLineEdit_712=tk.Entry(root)
        GLineEdit_712["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_712["font"] = ft
        GLineEdit_712["fg"] = "#333333"
        GLineEdit_712["justify"] = "center"
        GLineEdit_712["text"] = "Admin"
        GLineEdit_712.place(x=440,y=10,width=70,height=25)

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
                            # TODO chequear el rol del usuario para abrir el menu/ventana correspondiente
                            print("Mostrar pantalla para usuario con rol de Cliente")
                    else:
                        tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
                else:
                    tkMsgBox.showwarning(self.master.title(), "Usuario/Contraseña incorrecta")
            else:
                tkMsgBox.showwarning(self.master.title(), "Ingrese el Usuario para iniciar sesión")
        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))


    def cancelar(self):
        self.destroy()


    def abrir_user(self):
        User(self.master)