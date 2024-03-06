INSERT INTO Usuario(id_usuario, Nombre, Apellido, domicilio, contrasena, email)
VALUES 
('Usuario1', 'Usu', 'Ario', 'Barrio Golf Calle 3', 'password', 'email@gmail.com');

INSERT INTO Pedido (id_pedido, monto, mediodepago, fecha, n_de_factura, id_usuario, id_producto)
value
('1', '150', 'transferencia', '2000-01-01', '000100000001','Usuario1','1'),
('2', '200', 'credito', '2001-01-01', '000100000002', 'Usuario2','2'),
('3', '250', 'debito', '2002-02-02', '000100000003','Usuario3', '3'),
('4', '300', 'pendiente', '2003-03-03', '000100000004','Usuario4','4');

INSERT INTO Categoria (id_categoria, nombre_categoria)
value 
('123', 'Electrohogar'),
('345', 'Computacion'),
('567', 'Telefonia'),
('789', 'Sonido');

INSERT INTO Producto (id_producto, nombre, stock, marca, descripcion, precio, id_categoria)
value
('10', 'reloj', '15', 'casio', '....', '250USD', '123'),
('20', 'computadora', '5', 'lenovo', 'ryzen 7', '900USD', '345'),
('30', 'celular', '90', 'huawei', '....', '300USD', '567'),
('40', 'auriculares', '3', 'audio technica', '....', '99USD', '789'),

