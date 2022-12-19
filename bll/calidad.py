from dal.db import Db

def listar():
    sql = "SELECT calidad_Id, Nombre FROM Calidad ORDER BY calidad_Id;"
    result = Db.consultar(sql)
    return result