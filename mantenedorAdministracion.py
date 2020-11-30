import pymysql
from claseCliente import Cliente

def conectar():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='',
                                   db = 'carcastore')
    except:
        print("Error de conexion")
    return conexion

def  insertar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO cliente (rut,nombre,correo,clave) VALUES (%s,%s,%s,%s);"
            cursor.execute(consulta,(cliente.rut,cliente.nombre,cliente.correo,cliente.clave))
            conexion.commit()
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()

def consultar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM cliente")
            #usamos fetchall para traer todos los datos
            auxCliente = cursor.fetchall()
            #recorremos
            for cli in auxCliente:
                print(cli)
            return auxCliente
    #final
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Ocurrio un error al insertar ",ex) 
    conexion.close()


#programa principal
conectar()
print("Conectado")
#auxCliente = Cliente("19334455-7", "francisco", "fran31@hotmail.com", "franbacan")
#insertar(auxCliente)
#print("Datos ingresados")
consultar()