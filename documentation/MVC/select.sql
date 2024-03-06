select *from usuario;
select *from producto;
select *from pedido;

select *from pedido where id_usuario='Usuario1';
select *from pedido where fecha='2000-01-01';

select *from pedido where monto>'5000';
select max(monto) from pedido;
select min(monto) from pedido;

select max(precio), marca from producto;
select min(precio), marca from producto;




