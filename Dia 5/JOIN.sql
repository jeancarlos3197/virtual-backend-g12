-- JOINS
-- es la manera de ingresar desde una tabla hacia otra mediante una col en común
USE prueba;

SELECT * FROM vacunatorio INNER JOIN vacunas ON vacunatorio.vacuna_id = vacunas.id; 
-- WHERE vacuna_id=1;

-- left esto traera todo el contenido de la tabla de la izquierda, opcionalemente con la tabla de la derecha
SELECT * FROM VACUNATORIO LEFT JOIN VACUNAS ON VACUNATORIO.vacuna_id = VACUNAS.ID;

SELECT * FROM VACUNATORIO RIGHT JOIN VACUNAS ON VACUNATORIO.vacuna_id = VACUNAS.ID;

SELECT * FROM VACUNATORIO LEFT JOIN VACUNAS ON VACUNATORIO.vacuna_id = VACUNAS.ID UNION
SELECT * FROM VACUNATORIO RIGHT JOIN VACUNAS ON VACUNATORIO.vacuna_id = VACUNAS.ID;

-- INSERT INTO vacunatorio (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
--                       ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null);

SELECT * FROM VACUNATORIO AS VAC JOIN VACUNAS AS VACU ON VAC.vacuna_id = VACU.ID WHERE VACU.NOMBRE = 'Pfizer';

-- 1. Devolver todos los vacunatorios en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
SELECT * 
FROM vacunatorios JOIN vacunas on vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre='SINOPHARM' AND horario_atencion LIKE '%LUN-VIE%';

-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00
SELECT vacunas.nombre
FROM vacunatorio JOIN vacunas on vacunatorio.vacuna_id = vacunas.id
WHERE latitud BETWEEN -5 AND 10 ;

SELECT vacunas.nombre
FROM vacunatorio JOIN vacunas on vacunatorio.vacuna_id = vacunas.id
WHERE latitud > -5 AND latitud < 10 ;

-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente mostrar su procedencia y nombre
SELECT procedencia, vacunas.nombre 
FROM vacunatorio RIGHT JOIN vacunas on vacunatorio.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;