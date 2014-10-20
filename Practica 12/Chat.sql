--Script para practica 14

drop table Mensajes cascade;
drop table Canales cascade;
drop table EstadosCanales cascade;
drop table Usuarios cascade;

create table Usuarios(
	Id serial primary key,
	Nombre varchar(50) not null
);

create table EstadosCanales(
	Id serial primary key, 
	Nombre varchar(50) not null
);

create table Canales(
	Id Serial primary key,
	Nombre varchar(50) not null unique,
	EstadoCanalId int references EstadosCanales(Id)
);


create table Mensajes(
	Id Serial primary key,
	UsuarioId int not null references Usuarios(Id),
	CanalId int not null references Canales(Id),
	Mensaje text,
	FechaEnviado timestamp not null
);

