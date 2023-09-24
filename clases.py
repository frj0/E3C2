class Usuario:
    def __init__(self, nombre_usuario, correo_electronico, contrasena):
        self.nombre_usuario = nombre_usuario
        self.correo_electronico = correo_electronico
        self.contrasena = contrasena

class Producto:
    def __init__(self, nombre, descripcion, precio, stock):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock

class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

class Venta:
    def __init__(self, fecha, usuario, productos):
        self.fecha = fecha
        self.usuario = usuario
        self.productos = productos

class Comentario:
    def __init__(self, contenido, usuario, fecha):
        self.contenido = contenido
        self.usuario = usuario
        self.fecha = fecha


class Proveedor:
    def __init__(self, nombre_empresa, detalles_contacto):
        self.nombre_empresa = nombre_empresa
        self.detalles_contacto = detalles_contacto
