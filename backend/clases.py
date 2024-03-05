class Usuario:
    def __init__(self, nombre_usuario, correo_electronico, contrasena, domicilio, apellido, nombre):
        self.nombre_usuario = nombre_usuario
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena
        self.domicilio = domicilio

class Producto:
    def __init__(self, nombre_producto, descripcion, precio, stock, marca, categoria):
        self.nombre_producto = nombre_producto
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.marca = marca
        self.categoria = categoria


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def calcular_monto(self):
        monto = 0
        for producto in self.productos:
            monto += producto.precio
        return monto

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria
