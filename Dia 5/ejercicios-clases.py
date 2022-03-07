from datetime import datetime
# crear una clase Persona en la cual se guarden su nombre, fecha_nacimiento, nacionalidad, dni, ademas tambien una clase Alumno y una clase Docente en la cual el alumno , a diferencia del docente, tenga una serie de cursos matriculados, y el docente por su parte tenga un numero del seguro social y su cuenta de la CTS. En base a lo visto de herencia codificar las clases y ademas ver si hay algun atributo o metodo que deba de ser privado.
class Persona:
  def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni):
      self.nombre=nombre
      self.fecha_nacimiento=fecha_nacimiento
      self.nacionalidad=nacionalidad
      self.dni=dni

  def descripcion(self):
    return 'Me llamo {}, naci el: {} , soy de {}, mi identificación es {}'.format(
      self.nombre,
      self.fecha_nacimiento,
      self.nacionalidad,
      self.dni
      )

class Alumno(Persona):
  def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni,cursos):
      super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
      self.cursos=cursos

  def info(self):
    return {
      'Alumno': self.descripcion(),
      'Cursos': self.cursos
    }

class Docente(Persona):
  def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni,seguro_social,cts):
      super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
      self.seguro_social=seguro_social
      self.cts=cts

  def info(self):
    return{
      'Docente': self.descripcion(),
      'Seguro Social': self.seguro_social,
      'CTS': self.cts
    }

alumno1 = Alumno('Jean',datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'Peruano','54781245',['matematica','comunicacion'])   
docente1 = Docente('carlos',datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'Colombiano','54741451','ESSALUD','25431654885')

print(alumno1.info())
print(docente1.info())