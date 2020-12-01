import pymysql
from clasesAdministracion import *

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db = 'administracion')
    except:
        print("Error de conexion")
    return conexion

#MANTENEDOR Empleado
def  insertarEmpleado(empleado):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO empleado (rut, nombres, apaterno, amaterno, edad, telefono, email) VALUES (%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(consulta,(empleado.rut, empleado.nombres, empleado.apaterno, empleado.amaterno, empleado.edad, empleado.telefono, empleado.email))
            conexion.commit()
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def consultarEmpleado():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM empleado")
            #usamos fetchall para traer todos los datos
            auxEmpleado = cursor.fetchall()
            #recorremos
            for emp in auxEmpleado:
                print(emp)
            return auxEmpleado
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def buscarEmpleado(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM empleado WHERE rut = %s;"
            cursor.execute(consulta,(auxRut))
            #usamos fetchall para traer todos los datos
            auxEmpleado = cursor.fetchall()
            #recorremos
            for emp in auxEmpleado:
                print(emp)
            return auxEmpleado
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al buscar",ex) 
    conexion.close()

def actualizarEmpleado(empleado):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE empleado SET rut = %s, nombres = %s, apaterno = %s, amaterno = %s, edad = %s, telefono = %s, email = %s WHERE rut = %s; "
            cursor.execute(consulta,(empleado.rut, empleado.nombres, empleado.apaterno, empleado.amaterno, empleado.edad, empleado.telefono, empleado.email, empleado.rut))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex) 
    conexion.close()

def eliminarEmpleado(auxRut):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM empleado WHERE rut = %s;"
            cursor.execute(consulta,(auxRut))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex) 
    conexion.close()

#conectar()
#print("Conectado")
#Insertar
#auxEmpleado = Empleado("20246110-7", "Henry Antonio", "Adasme", "Lopez", 19, 968288940, "fran31@hotmail.com")
#insertarEmpleado(auxEmpleado)
#print("Datos ingresados")

#Consultar
#consultarEmpleado()

#Buscar
#buscarEmpleado("20246110-7")

#Actualizar
#auxEmpleado = Empleado("20246110-7", "Henry Antonio", "Adasme", "Lopez", 20, 968288940, "he.adasme@alumnos.duoc.cl")
#actualizarEmpleado(auxEmpleado)
#buscarEmpleado("20246110-7")

#Eliminar
#eliminarEmpleado("20246110-7")


#MANTENEDORUsuario
def  insertarUsuario(usuario):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO usuario (nomusuario, email, contrasena) VALUES (%s,%s,%s);"
            cursor.execute(consulta,(usuario.nomusuario, usuario.email, usuario.contrasena))
            conexion.commit()
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def consultarUsuario():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuario")
            #usamos fetchall para traer todos los datos
            auxUsuario = cursor.fetchall()
            #recorremos
            for usu in auxUsuario:
                print(usu)
            return auxUsuario
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def buscarUsuario(auxEmail):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM usuario WHERE email = %s;"
            cursor.execute(consulta,(auxEmail))
            #usamos fetchall para traer todos los datos
            auxUsuario = cursor.fetchall()
            #recorremos
            for usuAd in auxUsuario:
                print(usuAd)
            return auxUsuario
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al buscar",ex) 
    conexion.close()

def actualizarUsuario(usuario):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE usuario SET nomusuario = %s, email = %s, contrasena = %s WHERE email = %s; "
            cursor.execute(consulta,(usuario.nomusuario, usuario.email, usuario.contrasena, usuario.email))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex) 
    conexion.close()

def eliminarUsuario(auxEmail):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM usuario WHERE email = %s;"
            cursor.execute(consulta,(auxEmail))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex) 
    conexion.close()


#programa principal
#conectar()
#print("Conectado")

#Insertar
#auxUsuario = Usuario("Henry", "fran31@hotmail.com", "franbacan")
#insertarUsuario(auxUsuario)
#print("Datos ingresados")

#Consultar
#consultarUsuario()

#Buscar
#buscarUsuario("fran31@hotmail.com")

#Actualizar
#auxUsuario = Usuario("Henry", "fran31@hotmail.com", "franbacan123")
#actualizarUsuario(auxUsuario)
#buscarUsuario("fran31@hotmail.com")

#Eliminar
#eliminarUsuario("fran31@hotmail.com")


#MANTENEDOR Producto
def  insertarProducto(producto):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO producto (idproducto, nomproducto, descripcion, precio, stock) VALUES (%s,%s,%s,%s,%s);"
            cursor.execute(consulta,(producto.idproducto, producto.nomproducto, producto.descripcion, producto.precio, producto.stock))
            conexion.commit()
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def consultarProducto():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM producto")
            #usamos fetchall para traer todos los datos
            auxProducto = cursor.fetchall()
            #recorremos
            for prod in auxProducto:
                print(prod)
            return auxProducto
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def buscarProducto(auxNomProducto):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM producto WHERE nomproducto = %s;"
            cursor.execute(consulta,(auxNomProducto))
            #usamos fetchall para traer todos los datos
            auxNomProducto = cursor.fetchall()
            #recorremos
            for nomprod in auxNomProducto:
                print(nomprod)
            return auxNomProducto
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al buscar",ex) 
    conexion.close()

def actualizarProducto(producto):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE producto SET idproducto = %s, nomproducto = %s, descripcion = %s, precio = %s, stock = %s WHERE idproducto = %s; "
            cursor.execute(consulta,(producto.idproducto, producto.nomproducto, producto.descripcion, producto.precio, producto.stock, producto.idproducto))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex) 
    conexion.close()

def eliminarProducto(auxId):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM producto WHERE idproducto = %s;"
            cursor.execute(consulta,(auxId))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex) 
    conexion.close()

conectar()
print("Conectado")

#Insertar
#auxProducto = Producto(1, "Carcasa", "Modelo Iphone 7 color azul", 2000, 9)
#insertarProducto(auxProducto)
#print("Datos ingresados")

#Consultar
#consultarProducto()

#Buscar
#buscarProducto("Carcasa")

#Actualizar
#auxProducto = Producto(1, "Carcasa", "Modelo Iphone XR color azul", 4000, 10)
#actualizarProducto(auxProducto)
#buscarProducto("Carcasa")

#Eliminar
#eliminarProducto(1)


#MANTENEDORUsuario
def  insertarProveedor(proveedor):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO proveedor (idproveedor, telefono, nomproveedor) VALUES (%s,%s,%s);"
            cursor.execute(consulta,(proveedor.idproveedor, proveedor.telefono, proveedor.nomproveedor))
            conexion.commit()
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def consultarProveedor():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM proveedor")
            #usamos fetchall para traer todos los datos
            auxProveedor = cursor.fetchall()
            #recorremos
            for prov in auxProveedor:
                print(prov)
            return auxProveedor
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def buscarProveedor(auxNomProveedor):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM proveedor WHERE nomproveedor = %s;"
            cursor.execute(consulta,(auxNomProveedor))
            #usamos fetchall para traer todos los datos
            auxNomProveedor = cursor.fetchall()
            #recorremos
            for prov in auxNomProveedor:
                print(prov)
            return auxNomProveedor
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al buscar",ex) 
    conexion.close()

def actualizarProveedor(proveedor):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "UPDATE proveedor SET idproveedor = %s, telefono = %s, nomproveedor = %s WHERE idproveedor = %s; "
            cursor.execute(consulta,(proveedor.idproveedor, proveedor.telefono, proveedor.nomproveedor, proveedor.idproveedor))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al actualizar",ex) 
    conexion.close()

def eliminarProveedor(auxId):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "DELETE FROM proveedor WHERE idproveedor = %s;"
            cursor.execute(consulta,(auxId))
            conexion.commit()
    
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al eliminar",ex) 
    conexion.close()


#programa principal
#conectar()
#print("Conectado")

#Insertar
#auxProveedor = Proveedor(1, 968288940, "FOXCON")
#insertarProveedor(auxProveedor)
#print("Datos ingresados")

#Consultar
#consultarProveedor()

#Buscar
#buscarProveedor("FOXCON")

#Actualizar
#auxProveedor = Proveedor(1, 968288940, "Apple")
#actualizarProveedor(auxProveedor)
#buscarProveedor("Apple")

#Eliminar
#eliminarProveedor(1)