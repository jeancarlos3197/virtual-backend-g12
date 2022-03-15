#factory
from faker import Faker
from random import randint, choice
# from faker.providers import internet, person
# usando el provider de person hacer que me imprime un nombre , ape_pat. ape_mat, correo(internet), num_telefonico(phone_number)
fake = Faker()
# Le agregamos un provider adicional a nuestro faker para que ahora pueda utilizar los tradicionales y los provider
# fake.add_provider({internet, person})

def generar_alumnos():
  for persona in range(100):
    nombre = fake.first_name()
    apePat = fake.last_name()
    apeMat = fake.last_name()
    correo = fake.ascii_email()
    telefono = fake.bothify(text='9########')

    sql = '''INSERT INTO ALUMNOS (NOMBRE, APELLIDO_PATERNO, APELLIDO_MATERNO, CORREO, NUMERO_EMERGENCIA) VALUES
                                ('%s', '%s', '%s', '%s', '%s');''' %(nombre, apePat, apeMat, correo, telefono)
    print(sql)
# generar_alumnos()    

def generar_niveles():
  secciones = ['A', 'B', 'C']
  ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
  niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
  #Iterar los niveles y en cada nivel colocar como minimo dos secciones y como maximo 3(random_int) y luego agregar aleatoriamente la ubicacion a ese nivel
  for nivel in niveles:
    pos_secciones = randint(2, 3)
    for posicion in range(0, pos_secciones):
      # pos_ubicaciones = fake.random_int(min=0, max=3)
      # ubicacion = ubicaciones[pos_ubicaciones]
      ubicacion = choice(ubicaciones)
      seccion = secciones[posicion]
      nombre = nivel
      sql = '''INSERT INTO NIVELES(SECCION, UBICACION, NOMBRE) VALUES
                            ('%s', '%s', '%s');''' % (seccion, ubicacion, nombre)
      print(sql)

# generar_niveles()
def generar_niveles_alumnos():
  # generar un numero aleatorio que sera el id del alumno y el id del nivel y un anio de manera en la cual no se puede volver a generar ese mismo alumno con un nivel inferior pero con un anio superior
    # ALUMNO_ID    NIVEL_ID    YEAR
    #     1            3        2000   // 3 > segundo A 
    #     1            1        1999   // 1 > primero A ✔️
    #     1            1        2002   // 1 > primero A ❌
    # en total tiene que haber unos 80 registros
  listaAl=[]
  for asig_alu in range(80):
    alumno = fake.random_int(min=1, max=100)
    alu_niv = fake.random_int(min=2, max=3)
    listaS=[]
    for asig_niv in range(alu_niv):
      nivel = fake.random_int(min=1, max=15)
      # listaS.append({
      #   'anio':anio,
      #   'nivel':nivel
      # })
      
      if nivel<=3:
        anio = fake.date(pattern='%Y')

        if listaS['anio'] is None :
          listaS.append({
            'anio':anio,
            'nivel':nivel
          })
        else:
          if anio == listaS['anio']:
            listaS.append({
              'anio':anio,
              'nivel':nivel
            })
          if anio < listaS['anio']:
            break

      elif nivel <=5:
        pass
      elif nivel <=8:
        pass
      elif nivel <=10:
        pass
      elif nivel <=12:
        pass 
      elif nivel <=15:
        pass
    listaAl.append({
      'alumno':alumno,
      'ani_niv':listaS
    })
    print(listaAl)


generar_niveles_alumnos()