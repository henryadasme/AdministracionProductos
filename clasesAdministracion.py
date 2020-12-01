class Empleado:
    def __init__(self ,rut ,nombres, apaterno, amaterno, edad, telefono, email):
        self.rut = rut
        self.nombres = nombres
        self.apaterno = apaterno 
        self.amaterno = amaterno
        self.edad = edad
        self.telefono = telefono
        self.email = email

class Usuario:
    def __init__(self, nomusuario, email, contrasena):
        self.nomusuario = nomusuario
        self.email = email
        self.contrasena = contrasena

class Producto:
    def __init__(self, idproducto, nomproducto, descripcion, precio, stock):
        self.idproducto = idproducto
        self.nomproducto = nomproducto
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

class Proveedor:
    def __init__(self, idproveedor, telefono, nomproveedor):
        self.idproveedor = idproveedor
        self.telefono = telefono
        self.nomproveedor = nomproveedor

#auxCliente = Cliente("19942321-4","alvaro","yankee_24@hotmail.com","pajenry123")
#print(auxCliente.rut)