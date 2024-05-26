drop database if exists vitamilk_db;
show databases;


create database vitamilk_db;

use vitamilk_db;almacenesalmacenesalmacenes

CREATE TABLE Productos_Lacteos (
    ID_Producto INT PRIMARY KEY,
    Nombre_Producto VARCHAR(255),
    Fecha_Vencimiento DATE,
    Proveedor VARCHAR(255),
    Cantidad_Stock INT,
    Precio_Unitario DECIMAL(10)
    );


CREATE TABLE Almacenes (
    ID_Almacen INT PRIMARY KEY,
    Nombre_Almacen VARCHAR(255),
    Ubicacion VARCHAR(255),
    Capacidad_Maxima INT
);

CREATE TABLE Movimientos_Inventarios (
    ID_Movimiento INT PRIMARY KEY,
    Fecha_Hora DATETIME,
    Tipo_Movimiento VARCHAR(50),
    ID_Producto INT,
    ID_Almacen INT,
    Cantidad_Movida INT,
    FOREIGN KEY (ID_Producto) REFERENCES Productos_Lacteos(ID_Producto),
    FOREIGN KEY (ID_Almacen) REFERENCES Almacenes(ID_Almacen)
);

CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY,
    Nombre_Cliente VARCHAR(255),
    Direccion VARCHAR(255),
    Informacion_Contacto VARCHAR(255)
);

CREATE TABLE Pedidos (
    ID_Pedido INT PRIMARY KEY,
    ID_Cliente INT,
    Fecha_Pedido DATE,
    Estado_Pedido VARCHAR(50),
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);

