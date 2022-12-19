import sqlite3
from datetime import date
import hashlib

database = "Cinemar.db" # todo: por ahora ponemos el nombre de la base aqui, ver mejor opcion

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
                                "IdUsuario"	INTEGER NOT NULL,
                                "Apellido"	VARCHAR(50),
                                "Nombre"	VARCHAR(50),
                                "FechaNacimiento"	VARCHAR(23),
                                "Dni"	INTEGER,
                                "CorreoElectronico"	VARCHAR(50),
                                "Usuario"	VARCHAR(15) UNIQUE,
                                "Contrasenia"	VARCHAR(100),
                                "IdRol"	INTEGER,
                                "Activo"	INTEGER NOT NULL DEFAULT 1,
                                "Vip"	INTEGER NOT NULL DEFAULT 0,
                                PRIMARY KEY("IdUsuario" AUTOINCREMENT)
                            );'''
        sql_roles = '''CREATE TABLE IF NOT EXISTS "Roles" (
                            "IdRol"	INTEGER NOT NULL,
                            "Nombre"	VARCHAR(30) NOT NULL UNIQUE,
                            "Activo"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("IdRol")
                        );'''
        sql_salas = '''CREATE TABLE IF NOT EXISTS "Salas" (
	                        "IdSala"	INTEGER NOT NULL,
	                        "NombreSala"	TEXT NOT NULL UNIQUE,
                            "Tipo"	TEXT NOT NULL,
                            "Capacidad"	INTEGER NOT NULL,
                            "Activo"    INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("IdSala" AUTOINCREMENT)
                        );'''
        sql_peliculas = '''CREATE TABLE IF NOT EXISTS "Peliculas" (
                            "IdPelicula"	INTEGER NOT NULL,
                            "NombrePelicula"	TEXT NOT NULL,
                            "Genero"	TEXT NOT NULL,
                            "Idioma"	TEXT NOT NULL,
                            "Clasificacion"	TEXT NOT NULL,
                            "Activa"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("IdPelicula" AUTOINCREMENT)
                        );'''

        sql_funciones = '''CREATE TABLE IF NOT EXISTS "Funciones" (
                            "IdFuncion"	INTEGER NOT NULL,
                            "Fecha"	TEXT NOT NULL,
                            "Hora"	TEXT NOT NULL,
                            "IdSala"	INTEGER NOT NULL,
                            "IdPelicula"	INTEGER NOT NULL,
                            "Precio"	INTEGER NOT NULL,
                            "Activa"	INTEGER NOT NULL DEFAULT 1,
                            PRIMARY KEY("IdFuncion" AUTOINCREMENT)
                        );'''
        sql_Reserva = ''' CREATE TABLE IF NOT EXISTS "Reserva" (
	                        "Idreserva"	INTEGER NOT NULL,
	                        "IdPeli"	INTEGER NOT NULL,
	                        "fecha"	TEXT(30) NOT NULL,
                            "Idioma" TEXT(30) NOT NULL,
	                        "hora"	TEXT(50) NOT NULL,
	                        "Activo"	INTEGER NOT NULL DEFAULT 1,
	                        PRIMARY KEY("Idreserva" AUTOINCREMENT)
                        )'''

        tablas = {"Usuarios": sql_usuarios, "Roles": sql_roles, "Salas": sql_salas, "Peliculas": sql_peliculas, "Funciones": sql_funciones,"Reserva": sql_Reserva}

        with sqlite3.connect(database) as cnn:
            cursor = cnn.cursor()
            for tabla, sql in tablas.items():
                print(f"Creando tabla {tabla}")
                cursor.execute(sql)
            
    @staticmethod
    def poblar_tablas():        
        sql_roles = '''INSERT INTO Roles (IdRol, Nombre) 
                    VALUES 
                        (1, "Administrador"),
                        (2, "Supervisor"),
                        (3, "Operador"),
                        (4, "Cliente");'''

        sql_salas = '''INSERT INTO Salas (NombreSala, Tipo, Capacidad)
                    Values 
                        ("1", "2D", 50),
                        ("2", "3D", 60),
                        ("3", "4D", 40),
                        ("4", "IMAX", 50);'''
            
        sql_peliculas = '''INSERT INTO Peliculas (NombrePelicula, Genero, Idioma, Clasificacion)
                    Values 
                        ("Avatar", "Aventura", "Ingles", "+16"),
                        ("John Wick", "Accion", "Ingles", "+18"),
                        ("Minions", "Comedia", "Español", "ATP"),
                        ("El Conjuro 4", "Terror", "Ingles", "+16");'''
        

        tablas = {"Salas": sql_salas, "Roles": sql_roles, "Peliculas": sql_peliculas,} 

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