/* ==========================================================
Script de creación de tabla y procedimientos CRUD
Base de datos: tbl_account
Autor: Gabriela Descripción: Manejo de cuentas con nombre y fecha de nacimiento
Buenas prácticas aplicadas: 
- Uso de PRIMARY KEY con IDENTITY para clave única autoincremental 
- Restricción UNIQUE para evitar duplicados en fullname + birthdate 
- Procedimientos almacenados separados para cada operación CRUD 
- Uso de SET NOCOUNT ON para evitar mensajes innecesarios 
============================================================ */ 

-- Creación de tabla principal -- 
create table tbl_account (
	id int identity (1,1) primary key,
	fullname varchar(50) not null,
	birthdate date not null,
	constraint UQ_fullname_birthdate unique (fullname, birthdate)
);

-- Procedimientos almacenados para operaciones CRUD -- 

-- Procedimiento: Crear registro
create procedure csp_create_account
	
	@fullname varchar(50),
	@birthdate date
as
begin 
	set nocount on;
	insert into tbl_account(fullname, birthdate) values (@fullname, @birthdate);
end;
go 

-- Procedimiento: Leer registros
create procedure csp_read_account 
as 
begin 
	set nocount on;
	select id, fullname, birthdate
	from tbl_account
	order by id asc;
end;
go 

-- Procedimiento: Actualizar registro
create procedure csp_update_account 
	
	@id int,
	@fullname varchar(50),
	@birthdate date
as 
begin 
	set nocount on;
	update tbl_account 
	set fullname = @fullname, birthdate = @birthdate where id = @id;
end;
go

-- Procedimiento: Eliminar registro
create procedure csp_delete_account
	@id int
as
begin 
	set nocount on;
	delete from tbl_account where id = @id;
end;
