import sqlite3
from datetime import date
import hashlib

database = "CINEMARK--ARCA.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

class Db:
    @staticmethod
    def ejecutar(consulta, parametros = ()):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, parametros)
            cnn.commit()            
    
    @staticmethod
    def consultar(consulta, pametros = (), fetchAll = True):
        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            cursor.execute(consulta, pametros)
            if fetchAll:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            return result
    
    @staticmethod
    def crear_tablas():
        sql_usuarios = '''CREATE TABLE IF NOT EXISTS "Usuarios" (
                                "UsuarioId"	INTEGER NOT NULL,
                                "Apellido"	VARCHAR(50),
                                "Nombre"	VARCHAR(30),
                                "FechaNacimiento"	VARCHAR(23),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(30),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(100),
                                "RolId"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                PRIMARY KEY("UsuarioId" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "RolId"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("RolId")
                        );'''
        sql_Reserva = ''' CREATE TABLE IF NOT EXISTS "Reserva" (
	                        "Idreserva"	INTEGER NOT NULL,
	                        "IdPeli"	INTEGER NOT NULL,
	                        "fecha"	TEXT(30) NOT NULL,
	                        "hora"	TEXT(50) NOT NULL,
	                        "Activo"	INTEGER NOT NULL DEFAULT 1,
	                        PRIMARY KEY("Idreserva" AUTOINCREMENT)
                        )'''
        sql_Peliculas = '''CREATE TABLE IF NOT EXISTS "Peliculas" (
	                        "IdPelicula"	INTEGER NOT NULL,
	                        "NombrePelicula"	TEXT NOT NULL,
	                        "Genero"	TEXT NOT NULL,
	                        "Idioma"	TEXT NOT NULL,
	                        "Clasificacion"	TEXT NOT NULL,
                            "CalidadId"	INTEGER,
	                        "Activa"	INTEGER NOT NULL DEFAULT 1,
                        	PRIMARY KEY("IdPelicula" AUTOINCREMENT)
                        );'''
        sql_calidad = '''CREATE TABLE IF NOT EXISTS "Calidad" (
                            "calidad_Id"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("calidad_Id")
                        );'''

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles, "reserva": sql_Reserva, "Pelicula": sql_Peliculas }
        

        with sqlite3.connect(database) as cnn :
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
            cnn.commit
            
        
                # TODO agregar commit
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (RolId, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        tablas = {"Roles": sql_roles}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Poblando tabla {tabla}")
                cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
                count = int(cursor.fetchone()[0])
                if count == 0:
                    cursor.execute(sql)

    @staticmethod
    def formato_fecha_db(fecha):
        return date(int(fecha[6:]), int(fecha[3:5]), int(fecha[0:2]))
    
    @staticmethod
    def encriptar_contraseña(contrasenia):
        return hashlib.sha256(contrasenia.encode("utf-8")).hexdigest()