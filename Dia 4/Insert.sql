-- INSERTAR DATA
USE prueba;

INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
                    ('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
                    ('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
                    ('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
                    ('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');
INSERT INTO vacunatorio (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
                        ('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);                    

#MOSTRAR LOS NOMBRES DE LAS VACUNAS
#MOSTRAR LAS VACUNAS QUE SEAN DE PROCEDENCIA USA
#MOSTRAR LAS VACUNAS QUE NO SEAN DE PROCEDENCIA USA
#MOSTRAR LAS VACUNAS QUE EN SU LOTE TENGAN LOS DIGITOS 'XC'
#MOSTRAR TODOS LOS VACUNATORIOS QUE TENGAN HORARIO DE ATENCION LOS DIAS MIERCOLES 
#MOSTRAR TODOS LOS VACUNATORIOS QIE TENGAN LA VACUNA_ID 1 PERO QUE TENGA FOTO

SELECT * FROM vacunas;
SELECT * FROM vacunas WHERE procedencia='USA';
SELECT * FROM vacunas WHERE NOT procedencia='USA';
SELECT * FROM vacunas WHERE lote LIKE '%XC%';
SELECT * FROM vacunatorio WHERE horario_atencion LIKE '%MIE%' OR horario_atencion LIKE 'LUN-VIE';
SELECT * FROM vacunatorio WHERE vacuna_id = 1 AND (foto LIKE '%');