from dal.db import Db

def listar():
    sql = "SELECT IdRol, Nombre FROM Roles ORDER BY IdRol;"
    result = Db.consultar(sql)
    return result