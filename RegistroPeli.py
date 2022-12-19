from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.messagebox as tkMsgBox
import bll.peliculas as peli
import bll.calidad as Cal


class Peli (Toplevel):
    def __init__(self, master=None, isAdmin = False, peli_id = None):        
        super().__init__(master)
        self.master = master
        self.peli_id = peli_id 
        self.title("Registro Pelicula")
        #setting window size
        width=600
        height=500
        screenwidth = master.winfo_screenwidth()
        screenheight = master.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)

        GLabel_58=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#333333"
        GLabel_58["justify"] = "right"
        GLabel_58["text"] = "NombrePeli:"
        GLabel_58.place(x=40,y=80,width=102,height=31)

        GLineEdit_161=Entry(self, name="txtNombrePelicula")
        GLineEdit_161["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_161["font"] = ft
        GLineEdit_161["fg"] = "#333333"
        GLineEdit_161["justify"] = "center"
        GLineEdit_161["text"] = ""
        GLineEdit_161.place(x=220,y=80,width=289,height=30)

        GLabel_422=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_422["font"] = ft
        GLabel_422["fg"] = "#333333"
        GLabel_422["justify"] = "right"
        GLabel_422["text"] = "Genero:"
        GLabel_422.place(x=40,y=160,width=104,height=30)

        GLineEdit_957=Entry(self, name="txtGenero")
        GLineEdit_957["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_957["font"] = ft
        GLineEdit_957["fg"] = "#333333"
        GLineEdit_957["justify"] = "center"
        GLineEdit_957["text"] = ""
        GLineEdit_957.place(x=220,y=160,width=290,height=30)


        GLabel_615=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_615["font"] = ft
        GLabel_615["fg"] = "#333333"
        GLabel_615["justify"] = "right"
        GLabel_615["text"] = "Idioma:"
        GLabel_615.place(x=40,y=240,width=104,height=31)

        GLineEdit_280=Entry(self, name="txtIdioma")
        GLineEdit_280["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_280["font"] = ft
        GLineEdit_280["fg"] = "#333333"
        GLineEdit_280["justify"] = "center"
        GLineEdit_280["text"] = ""
        GLineEdit_280.place(x=220,y=240,width=290,height=30)

        GLabel_846=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_846["font"] = ft
        GLabel_846["fg"] = "#333333"
        GLabel_846["justify"] = "right"
        GLabel_846["text"] = "Clasificacion:"
        GLabel_846.place(x=40,y=320,width=106,height=30)        
                

        GLineEdit_857=Entry(self, name="txtClasificacion")
        GLineEdit_857["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_857["font"] = ft
        GLineEdit_857["fg"] = "#333333"
        GLineEdit_857["justify"] = "center"
        GLineEdit_857["text"] = ""
        GLineEdit_857.place(x=220,y=320,width=290,height=30)

        GLabel_406=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_406["font"] = ft
        GLabel_406["fg"] = "#333333"
        GLabel_406["justify"] = "right"
        GLabel_406["text"] = "Formato:"
        GLabel_406.place(x=40,y=380,width=155,height=33)

        calidad = dict(Cal.listar())
        if isAdmin:
            cb_roles = ttk.Combobox(self, state="readonly", values=list(calidad.values()), name="cbCalidad")
        else:
            cb_calidad = ttk.Combobox(self, state="disabled", values=list(calidad.values()), name="cbCalidad")
            cb_calidad.set(calidad[4])
        cb_calidad.place(x=140,y=380,width=283,height=30)

        GButton_31=Button(self)
        GButton_31["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_31["font"] = ft
        GButton_31["fg"] = "#000000"
        GButton_31["justify"] = "center"
        GButton_31["text"] = "aceptar"
        GButton_31.place(x=290,y=420,width=122,height=42)
        GButton_31["command"] = self.aceptar

        GButton_478=Button(self)
        GButton_478["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_478["font"] = ft
        GButton_478["fg"] = "#000000"
        GButton_478["justify"] = "center"
        GButton_478["text"] = "cancelar"
        GButton_478.place(x=430,y=420,width=122,height=42)
        GButton_478["command"] = self.cancelar

        GLabel_477=Label(self)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_477["font"] = ft
        GLabel_477["fg"] = "#333333"
        GLabel_477["justify"] = "center"
        GLabel_477["text"] = "Registro de pelicula"
        GLabel_477.place(x=30,y=10,width=156,height=30)


        if peli_id is not None:
            pelicula = peli.obtener_id(peli_id)
            if pelicula is None:
               tkMsgBox.showerror(self.master.title(), "Se produjo un error al obtener los datos del usuario, reintente nuevamente")
               self.destroy()
            else:
                GLineEdit_161.insert(0, pelicula[1])
                GLineEdit_957.insert(0, pelicula[2])
                GLineEdit_280.insert(0, pelicula[2])
                GLineEdit_857.insert(0, pelicula[4])
                


    def get_value(self, name):
        return self.nametowidget(name).get()

    def get_index(self, name):
        return self.nametowidget(name).current() + 1

    def cancelar(self):
        self.destroy()

    def aceptar(self):
        try:            
            nombrepeli = self.get_value("txtNombrePelicula")
            genero = self.get_value("txtGenero")            
            idioma = self.get_value("txtIdioma")            
            clasificacion = self.get_value("txtClasificacion")
            calidadId = self.get_index("cbCalidad")
        
                       
            if self.peli_id is None:
                print("Pelicula agregada")
                peli.agregar(nombrepeli, genero, idioma, clasificacion, calidadId)
                tkMsgBox.showinfo(self.master.title(), "Registro agregado!!!!!!")                
                try:
                    self.master.refrescar()
                except Exception as ex:
                        print(ex)
               
                self.destroy()                
                
            else:
                print("Actualizacion de Peliculas")
                peli.actualizar(self.peli_id, nombrepeli, genero, idioma, clasificacion, calidadId)  # TODO ver el tema de la contraseña
                tkMsgBox.showinfo(self.master.title(), "Registro modificado!!!!!!")                
                self.master.refrescar()
                self.destroy()  

        except Exception as ex:
            tkMsgBox.showerror(self.master.title(), str(ex))

