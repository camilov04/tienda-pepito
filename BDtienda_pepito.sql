/*crar base de datos*/
create database TiendaPepito;
use tiendaPepito;

/*crear tabla de los clientes*/
create table cliente(
codigocliente int primary  key not null auto_increment ,
 nombre char(20) not null,
 apellido char(20) not null,
 telefono char(10) not null,
 saldocuenta float
);

/*crear tabla del login para inicio de sesion*/
create table login(
correo varchar(20) primary  key not null,
password varchar(255) not null
);

/* para insertar el registro del tendero para poderse logear*/
insert into login(correo, password)
value('hugo@sena.edu.co', '123');


