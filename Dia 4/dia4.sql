USE prueba;

-- Sub parte SQL:
-- DML: Data Manipulation Language (Lenguaje de Manipulacion de Datos)
-- Se utiliza para la manipulacion de la informacion dentro de la base de datos
-- INSERT, SELECT, UPDATE, DELETE

INSERT INTO clientes(nombre, documento, tipo_documento, estado) VALUES
					('Jean','54124754', 'DNI',true);
INSERT INTO clientes(nombre, documento, tipo_documento, estado) VALUES
					('Carlos','84572415', 'DNI',true),
					('Fabian','5214741454', 'RUC',false); 

# SELECT: es el comando que sirve para visualizar la informacion de una determinada tabla o tablas
SELECT nombre, documento FROM clientes;

-- Si queremos observar todas las columnas de esa tabla(s)
SELECT * FROM clientes;

-- Al usar parentesis en una condicional, esas condiciones internas se ejecutaran primero para luego recien el resultado se compare con la condicion externa
SELECT * FROM clientes WHERE documento='54124754' AND (nombre = 'Jean' OR nombre = 'Carlos');

-- Seleccionar a todas las personas que tiene dni y que su estado sea tru
SELECT * FROM clientes WHERE tipo_documento='DNI' AND estado = true;
SELECT * FROM clientes WHERE nombre like 'Ca%s';

UPDATE clientes SET nombre = 'Ramiro', documento = '58471425' WHERE id = 1 AND nombre='Jean';

-- Desactivar modo seguro
SET SQL_SAFE_UPDATES = false;

-- Delete sirve para eleminar REGISTROS de una determinada tabla
DELETE FROM clientes WHERE id = 1;