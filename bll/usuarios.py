from dal.db import Db

def agregar(apellido, nombre, fecha_nacimiento, dni, correo_electronico, usuario, contrasenia, Id_rol):    
    sql = "INSERT INTO Usuarios(Apellido, Nombre, FechaNacimiento, Dni, CorreoElectronico, Usuario, Contrasenia, IdRol) VALUES(?, ?, ?, ?, ?, ?, ?, ?);"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, usuario, Db.encriptar_contraseña(contrasenia), Id_rol)
    Db.ejecutar(sql, parametros)

def actualizar(id, apellido, nombre, fecha_nacimiento, dni, correo_electronico, contrasenia, Id_rol):    
    sql = "UPDATE Usuarios SET Apellido = ?, Nombre = ?, FechaNacimiento = ?, Dni = ?, CorreoElectronico = ?, Contrasenia = ?, IdRol = ? WHERE IdUsuario = ? AND Activo = 1;"
    parametros = (apellido, nombre, Db.formato_fecha_db(fecha_nacimiento), dni, correo_electronico, Db.encriptar_contraseña(contrasenia), Id_rol, id)
    Db.ejecutar(sql, parametros)    

def eliminar(id, logical = True):    
    if logical:
        sql = "UPDATE Usuarios SET Activo = 0 WHERE IdUsuario = ? AND Activo = 1;"
    else:
        sql = "DELETE FROM Usuarios WHERE IdUsuario = ?;"
    parametros = (id,)
    Db.ejecutar(sql, parametros)


def obtener_nombre_usuario(usuario):
    sql = '''SELECT u.IdUsuario, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.IdRol, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.IdRol = r.IdRol
            WHERE u.Usuario = ? AND u.Activo = 1;'''
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)    
    return result

def listar():
    sql = '''SELECT u.IdUsuario, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.IdRol, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.IdRol = r.IdRol
            WHERE u.Activo = 1;'''
    result = Db.consultar(sql)
    return result

def filtrar(usuario):    
    sql = '''SELECT u.IdUsuario, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.IdRol, r.Nombre Rol
            FROM Usuarios u
            INNER JOIN Roles r ON u.IdRol = r.IdRol
            WHERE u.Usuario LIKE ? AND u.Activo = 1;'''    
    parametros = ('%{}%'.format(usuario),)    
    result = Db.consultar(sql, parametros)
    return result

def validar(usuario, contrasenia):    
    sql = "SELECT Usuario FROM Usuarios WHERE Usuario = ? AND Contrasenia = ? AND Activo = 1;"
    parametros = (usuario, Db.encriptar_contraseña(contrasenia))
    result = Db.consultar(sql, parametros, False)
    return result != None

def existe(usuario):
    sql = "SELECT COUNT(*) FROM Usuarios WHERE Usuario = ? AND Activo = 1;"
    parametros = (usuario,)
    result = Db.consultar(sql, parametros, False)
    count = int(result[0])
    return count == 1


def obtener_id(id):
    sql = '''SELECT u.IdUsuario, u.Apellido, u.Nombre, u.FechaNacimiento, u.Dni, u.CorreoElectronico, u.Usuario, u.IdRol, r.Nombre Rol
        FROM Usuarios u
        INNER JOIN Roles r ON u.IdRol = r.IdRol
        WHERE u.IdUsuario = ? AND u.Activo = 1;'''
    parametros = (id,)
    result = Db.consultar(sql, parametros, False)    
    return result