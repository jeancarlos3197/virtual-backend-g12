from config import conexion
from models.usuarios import Usuario
from bcrypt import checkpw

def autentificador(username, password):
  """ Función encargada de validar si las credenciales son correctas o no, si no son no pasara pero si si loson retornara una JWT """
  # primero valido si los parametros son correctos
  if username and password:
    usuarioEncontrado = conexion.session.query(Usuario).filter_by(correo=username).first()
    if usuarioEncontrado:
      # ahora valido si el password es la correcta
      validacion = checkpw(bytes (password, 'utf-8'), bytes (usuarioEncontrado.password, 'utf-8'))
      if validacion is True:
        return usuarioEncontrado
      else:
        return None
    else:
      return None
  else:
    return None

def identificador(payload):
  """ Sirve para validar al usuario previamente autenticado """
  # en el payload obtendremos la parte intermedia de la JWT que es la informacion que se puede visualizar sin la necesidad de saber la contraseña de la token
  # identity > la identificacion del usuario por lo general viene a ser el  id o uuid del mismo
  # select * from usuarios where id = ...
  usuarioEncontrado: Usuario | None = conexion.session.query(Usuario).filter_by(id = payload['identity']).first()
  if usuarioEncontrado:
    # esta información me servira para cuando quiera acceder al usuario actual de la petición 
    return usuarioEncontrado
  else:
    return None