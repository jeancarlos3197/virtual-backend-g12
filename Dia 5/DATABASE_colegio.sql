create database colegio;
use colegio;

-- alumno: nombre, apellido paterno, apellido materno, correo, numero de emergencia
-- seccion: nombre, ubicacion

CREATE TABLE ALUMNOS(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    NOMBRE VARCHAR(30) NOT NULL,
    APELLIDO_PATERNO VARCHAR(50) NOT NULL,
    APELLIDO_MATERNO VARCHAR(50) NOT NULL,
    CORREO VARCHAR(50) UNIQUE NULL,
    NUMERO_EMERGENCIA CHAR(9) NOT NULL
);

CREATE TABLE NIVELES(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    SECCION VARCHAR(45),
    UBICACION VARCHAR(45),
    NOMBRE VARCHAR(45)
);

CREATE TABLE ALUMNOS_NIVELES(
	ID INT PRIMARY KEY AUTO_INCREMENT,
    FECHA_CURSADA YEAR,
    ALUMNO_ID INT,
    NIVEL_ID INT,
    FOREIGN KEY (ALUMNO_ID) REFERENCES ALUMNOS(ID),
    FOREIGN KEY (NIVEL_ID) REFERENCES NIVELES(ID)
);