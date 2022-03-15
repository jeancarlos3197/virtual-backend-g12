#SQL > Structured Query Language
#Un registro es un conjunto de datos, y un dato es un valor que por si solo no dice nada

CREATE DATABASE prueba;
USE prueba;

#Rl nombre de las tablas siempre en plural, ya que llevara varios registros
CREATE TABLE clientes(
	id INT AUTO_INCREMENT PRIMARY KEY,
    #char(n) creara una columna que siempre ocupara n espacios de caracteres
    #varchar(n) crear una columna que podra tener como maximo n caracteres y  ocupara el espacio que necesita
    nombre VARCHAR(50) NOT NULL,
    #UNIQUE valor unico, no repetido.
    dni CHAR(8) UNIQUE,
    carnet_extranjeria VARCHAR(10) UNIQUE,
    documento VARCHAR(10) UNIQUE,
    tipo_documento ENUM('C.E.', 'DNI', 'RUC', 'PASAPORTE', 'C.M.', 'OTRO'),
    #BOOL podra se true or false
    estado BOOL
)
