class Empleado:
    def __init__(self ,rut ,nombres, apaterno, amaterno, edad, telefono, usuario_email):
        self.rut = rut
        self.nombres = nombres
        self.apaterno = apaterno 
        self.amaterno = amaterno
        self.edad = edad
        self.telefono = telefono
        self.usuario_email = usuario_email

class Usuario:
    def __init__(self, nomusuario, email, contrasena, empleado_rut):
        self.nomusuario = nomusuario
        self.email = email
        self.contrasena = contrasena
        self.empleado_rut = empleado_rut

class Producto:
    def __init__(self, idproducto, nomproducto, descripcion, precio, stock, proveedor_idproveedor):
        self.idproducto = idproducto
        self.nomproducto = nomproducto
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.proveedor_idproveedor = proveedor_idproveedor

class Proveedor:
    def __init__(self, idproveedor, telefono, nomproveedor, producto_idproducto):
        self.idproveedor = idproveedor
        self.telefono = telefono
        self.nomproveedor = nomproveedor
        self. producto_idproducto = producto_idproducto

#auxCliente = Cliente("19942321-4","alvaro","yankee_24@hotmail.com","pajenry123")
#print(auxCliente.rut)