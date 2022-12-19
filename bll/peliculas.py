from dal.db import Db

def listar():
    sql = '''SELECT IdPelicula, NombrePelicula, Genero, Idioma, Clasificacion
            from Peliculas
        Where Activa = 1'''
    result = Db.consultar(sql)
    return result


def obtener_id(id):
    sql = '''SELECT NombrePelicula, Genero, Idioma, Clasificacion
            from Peliculas
        WHERE IdPelicula = ? AND Activa = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(pelicula):
    sql = "SELECT COUNT(*) FROM Peliculas WHERE NombrePelicula = ? AND Activa = 1 ;"
    parametros = (pelicula,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1


def agregar(nombrepelicula, genero, idioma, clasificacion):    
    sql = "INSERT INTO Peliculas (NombrePelicula, Genero, Idioma, Clasificacion) VALUES(?, ?, ?, ?);"
    parametros = (nombrepelicula, genero, idioma, clasificacion)
    Db.ejecutar(sql, parametros)

def actualizar(id, nombrepelicula, genero, idioma, clasificacion):    
    sql = "UPDATE Peliculas SET NombrePelicula = ?, Genero = ?, Idioma = ?, Clasificacion = ? WHERE IdPelicula = ? ;"
    parametros = (nombrepelicula, genero, idioma, clasificacion, id)
    Db.ejecutar(sql, parametros) 


def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Peliculas SET Activa = 0 WHERE IdPelicula = ? AND Activa = 1;"
    else:
        sql = "DELETE FROM Peliculas WHERE IdPelicula = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)