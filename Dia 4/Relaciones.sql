CREATE TABLE vacunas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) UNIQUE NOT NULL,
    estado BOOL DEFAULT TRUE,
    fecha_vencimiento DATE,
    procedencia ENUM('USA','CHINA','RUSIA','UK'),
    lote VARCHAR(10)
);

CREATE TABLE vacunatorio(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(200),
    horario_atencion VARCHAR(100),
    
    vacuna_id INT,
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

-- DDL DATA DEFINITION LANGUAGE se usara para la definicion de donde se almacenaran los datos en mi db
-- RENAME TABLE, CREATE TABLE, CREATE DATABASE
-- DROP eliminar la tabla y su contenido a diferencia del DELETE que solo eliminara el contenido
-- DROP TABLE, DROP DATABASE

ALTER TABLE vacunatorio ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;
ALTER TABLE vacunatorio RENAME COLUMN imagen TO foto;

-- modify column cambiar  el tipo de dato y los configuraciones adicionales
-- No podremos cambiar el tipo de dato si ya hay informacion en esa columna y no corresponde con el nuevo tipo de dato
-- ALTER TABLE vacunatorio MODIFY COLUMN foto CHAR(100)
DESC clientes;
