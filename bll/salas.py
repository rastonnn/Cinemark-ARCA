from dal.db import Db

def listar():
    sql = '''SELECT IdSala, NombreSala, Tipo, Capacidad
            from Salas
        Where Activo = 1'''
    result = Db.consultar(sql)
    return result


def obtener_id(id):
    sql = '''SELECT NombreSala, Tipo, Capacidad
            from Salas
        WHERE IdSala = ? AND Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result

def existe(sala):
    sql = "SELECT COUNT(*) FROM Salas WHERE NombreSala = ? AND Activo = 1 ;"
    parametros = (sala,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1


def agregar(nombresala, tipo, capacidad):    
    sql = "INSERT INTO Salas(NombreSala, Tipo, Capacidad) VALUES(?, ?, ?);"
    parametros = (nombresala, tipo, capacidad)
    Db.ejecutar(sql, parametros)

def actualizar(id, nombresala, tipo, capacidad):    
    sql = "UPDATE Salas SET NombreSala = ?, Tipo = ?, Capacidad = ? WHERE IdSala = ? ;"
    parametros = (nombresala, tipo, capacidad, id)
    Db.ejecutar(sql, parametros) 


def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Salas SET Activo = 0 WHERE IdSala = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Sala WHERE IdSala = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)