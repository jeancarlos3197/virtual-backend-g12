from flask_restful import Resource, request
from config import conexion
from models.ingredientes import Ingrediente
# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase

class IngredientesController(Resource):
  def get(self):
    resultado = conexion.session.query(Ingrediente).all()
    print(resultado)
    return {
      'message':'Yo soy el get de los ingredientes',
      'content': {
        'id': resultado[0].id,
        'nombre': resultado[0].nombre
      }
    }

  def post(self):
    print(request.get_json())
    # registramos un nuevo ingrediente
    try:
      nuevoIngrediente = Ingrediente()
      nuevoIngrediente.nombre = 'Leche evaporada'

      # ahora guardamos la informacion en la base de datos
      conexion.session.add(nuevoIngrediente)
      # add > estamos creando una nueva transacción
      # commit > sirve para guardar los cambios de manera permanente en la bd
      conexion.session.commit()

      return {
        'message': 'ingrediente creado exitosamente'
      }
    except Exception as e:
      # si hubo algun error al momento de hacer alguna modificacion a la bd entonces 'retrocederemos' todos esas modificaciones y lo dejaremos sin ningun cambion
      conexion.session.rollback()
      return {
        'message': 'hubo un error al crear el ingrediente',
        'content': e.args[0]
      }