from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, correo, nombre, rol, password):
    """ Creacion de un usuario sin el comando createsuperuser """
    if not correo:
      raise ValueError('El usuario debe tener un correo')
    # normalizo el correo > aparte de validar que sea un correo valido removera los espacios innecesarios
    correo = self.normalize_email(correo)
    # manda a llamar al modelo Usuario e iniciara su construccion
    nuevoUsuario = self.model(correo = correo, nombre = nombre, rol = rol)
    # set_password > genera un hash de la contraseña usando bcrypt y el algoritmo SHA256
    nuevoUsuario.set_password(password) 
    # sirve para referencia a la base de datos x default en el caso que tengamos varias conexiones a diferentes bases de datos
    nuevoUsuario.save(using=self._db)
    # Pasar la documentación del profe
    return nuevoUsuario
  
  def create_superuser(self, correo, nombre, rol, password):
    usuario = self.create_user(correo, nombre, rol, password)
    # is_superuser > indicara que usuarios son super usuarios y podra acceder a todas las funcionalidades del panel administrativo
    usuario.is_superuser = True
    usuario.is_staff = True
    usuario.save(using=self._db)
