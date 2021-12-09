create database TiendaPepito;
use tiendaPepito;

create table cliente(
codigocliente int primary  key not null auto_increment ,
 nombre char(20) not null,
 apellido char(20) not null,
 telefono char(10) not null,
 saldocuenta float
);

create table login(
correo varchar(20) primary  key not null,
password varchar(255) not null
);


