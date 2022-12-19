from dal.db import Db

def agregar(nombrepeli, genero, idioma, clasificacion, calidad_Id):    
    sql = "INSERT INTO Peliculas(NombrePelicula, Genero, Idioma, Clasificacion, CalidadId) VALUES(?, ?, ?, ?, ?,?);"
    parametros = (nombrepeli, genero, idioma, clasificacion, calidad_Id)
    Db.ejecutar(sql, parametros)

def actualizar(id, nombrepeli, genero, idioma, clasificacion, calidad_Id, ):    
    sql = "UPDATE Peliculas SET NombrePelicula = ?, Genero = ?, Idioma = ?, Clasificacion = ?, CalidadId = ? WHERE IdPelicula = ? AND Activo = 1;"
    parametros = (nombrepeli, genero, idioma, clasificacion, calidad_Id,id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE peliculas SET Activo = 0 WHERE IdPelicula = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Peliculas WHERE IdPelicula = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)

def listar():
    sql = '''SELECT u.IdPelicula, u.NombrePelicula, u.Genero, u.Idioma, u.Clasificacion, u.CalidadId, r.Nombre Calidad
            FROM Peliculas u
            INNER JOIN Calidad r ON u.CalidadId = r.CalidadId
            WHERE u.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(pelicula):    
    sql = '''SELECT u.IdPelicula, u.NombrePelicula, u.Genero, u.Idioma, u.Clasificacion, u.CalidadId, r.Nombre Calidad
            FROM Peliculas u
            INNER JOIN Calidad r ON u.Calidad_Id = r.Calidad_Id
            WHERE u.NombrePelicula LIKE ? AND u.Activo = 1;'''    
    parametros = ('%{}%'.format(pelicula),)    
    result = Db.consultar(sql, parametros)
    return result

def existe(pelicula):
    sql = "SELECT COUNT(*) FROM Peliculas WHERE NombrePelicula = ? AND Activo = 1;"
    parametros = (pelicula,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1



def obtener_id(id):
    sql = '''SELECT u.IdPelicula, u.NombrePelicula, u.Genero, u.Idioma, u.Clasificacion, u.CalidadId, r.Nombre Calidad
            FROM Peliculas u
            INNER JOIN Calidad r ON u.CalidadId = r.CalidadId
            WHERE u.NombrePelicula = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def obtener_nombrepeli_pelicula(pelicula):
    sql = '''SELECT u.IdPelicula, u.NombrePelicula, u.Genero, u.Idioma, u.Clasificacion, u.CalidadId, r.Nombre Calidad
            FROM Peliculas u
            INNER JOIN Calidad r ON u.CalidadId = r.CalidadId
            WHERE u.NombrePelicula = ? AND u.Activo = 1;'''
    parametros = (pelicula,)
    result = Db.consultar(sql, parametros, False)    
    return result