from dal.db import Db

def listar():
    sql = '''select f.IdFuncion, p.NombrePelicula, p.Idioma, s.NombreSala, f.Fecha, F.Hora, s.Tipo, p.Clasificacion, f.Precio
            from Funciones f INNER JOIN Salas s, Peliculas p
        WHERE f.IdSala = s.IdSala AND f.IdPelicula = p.IdPelicula AND f.Activa = 1;'''
    result = Db.consultar(sql)
    return result

def listar_peliculas():
    sql = '''SELECT p.IdPelicula, p.NombrePelicula
            FROM Peliculas p
            Where p.Activa = 1;'''
    result = Db.consultar(sql)
    return result

def listar_salas():
    sql = '''SELECT s.IdSala, s.NombreSala
            FROM Salas s
            Where s.Activo = 1;''' 
    result = Db.consultar(sql)
    return result

def obtener_id(id):
    sql = '''select f.IdFuncion, p.NombrePelicula, p.Idioma, s.NombreSala, f.Fecha, F.Hora, s.Tipo, p.Clasificacion, f.Precio
            from Funciones f INNER JOIN Salas s, Peliculas p
        WHERE f.IdFuncion = ? AND f.IdSala = s.IdSala AND f.IdPelicula = p.IdPelicula AND f.Activa = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(idpelicula, idsala, fecha, hora):    #TODO NO ESTA CONTROLANDO BIEN SI EXISTE LA PELICULA
    sql = "SELECT count (*) FROM Funciones f WHERE f.IdPelicula = ? AND f.IdSala = ? AND f.Fecha = ? AND f.Hora = ?;"
    parametros = (idpelicula, idsala, fecha, hora)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1

def agregar(fecha, hora, idsala, idpelicula, precio):    
    sql = "INSERT INTO Funciones (Fecha, Hora, IdSala, IdPelicula, Precio) VALUES(?, ?, ?, ?, ?);"
    parametros = (fecha, hora, idsala, idpelicula, precio)
    Db.ejecutar(sql, parametros)

def actualizar(id, fecha, hora, idsala, idpelicula, precio):    
    sql = "UPDATE Funciones SET Fecha = ?, Hora = ?, IdSala = ?, IdPelicula = ?, Precio = ? WHERE IdFuncion = ? ;"
    parametros = (fecha, hora, idsala, idpelicula, precio, id)
    Db.ejecutar(sql, parametros) 


def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Funciones SET Activa = 0 WHERE IdFuncion = ? AND Activa = 1;"
    else:
        sql = "DELETE FROM Funciones WHERE IdFuncion = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)