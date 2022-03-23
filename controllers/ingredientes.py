from logging import exception
from flask_restful import Resource, request
from marshmallow.exceptions import ValidationError

from config import conexion
from models.ingredientes import Ingrediente
from dtos.dto_prueba import ValidadorPrueba, ValidadorUsuarioPrueba
from dtos.ingrediente_dto import IngredienteRequestDTO, IngredienteResponseDTO
# from marshmallow import validate
# todos los metodos HTTP que vamos a utilizar se definen como metodos de la clase

class IngredientesController(Resource):
  def get(self):
    resultado = conexion.session.query(Ingrediente).all()
    print(resultado)
    # si nosotros queremos convertir la informacion y es mas de 1, colocar many=True, esto se encargara de iterar y mostrar 
    ingredientesSerializados = IngredienteResponseDTO(many=True).dump(resultado)
    return {
      'message':'Yo soy el get de los ingredientes',
      'content': ingredientesSerializados
    }

  def post(self):
    print(request.get_json())

    data = request.get_json()

    # registramos un nuevo ingrediente
    try:      
      # validara que la data que el usuario me esta enviando cumpla con todos las caracteristicas de mi modelo (que sea un string , que no sea muy largo (mas de 45))
      data_serializada = IngredienteRequestDTO().load(data)
      print(data_serializada)
      nuevoIngrediente = Ingrediente()
      nuevoIngrediente.nombre = data_serializada.get('nombre')

      # ahora guardamos la informacion en la base de datos
      conexion.session.add(nuevoIngrediente)
      # add > estamos creando una nueva transacción
      # commit > sirve para guardar los cambios de manera permanente en la bd
      conexion.session.commit()
      ingredienteSerializado = IngredienteResponseDTO().dump(nuevoIngrediente)

      return {
        'message': 'ingrediente creado exitosamente',
        'ingrediente': ingredienteSerializado
      }, 201
    except ValidationError as e:
      return {
        'message': 'La informacion es incorrecta',
        'content': e.args
      }, 400
    except Exception as e:
      # si hubo algun error al momento de hacer alguna modificacion a la bd entonces 'retrocederemos' todos esas modificaciones y lo dejaremos sin ningun cambion
      conexion.session.rollback()
      return {
        'message': 'hubo un error al crear el ingrediente',
        'content': e.args[0]
      }, 500

class PruebaController(Resource):
  def post(self):
    data = request.get_json()
    try:
      validacion = ValidadorPrueba().load(data)
      # validacionLongitud = validate.Length(max = 10)
      # validacionLongitud(validacion.get('nombre'))
      # si todo fue exitoso y las validaciones pasaran bien entonces nos devolveran un diccionario con todos las llaves con sus valores
      print(validacion)
      return {
        'message':'ok',
        'data': validacion
      }
    except Exception as e:
      print(e.args)
      return {
        'message': 'error al recibir los datos',
        'contenido':e.args
      }
  def get(self):
    usuario = {
      'nombre': 'Eduardo',
      'apellido': 'Manrique',
      'nacionalidad': 'Peru',
      'password': 'mimamamemima123'
    }
    resultado = ValidadorUsuarioPrueba().dump(usuario)
    return{
      'message': 'El usuario es',
      'content': usuario,
      'resultado': resultado
    }

class IngredienteController(Resource):
  def get(self, id):

    ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
    
    if ingrediente:
      resultado = IngredienteResponseDTO().dump(ingrediente)
      return{
        'resulta': resultado
      }
    else:
      return {
        'message': 'El ingrediente a buscar no existe'
      }, 404
  def put(self, id):
    ingrediente = conexion.session.query(Ingrediente).filter_by(id=id).first()
    
    try:
      if ingrediente:
        body = request.get_json()
        data_validada = IngredienteRequestDTO().load(body)
        ingrediente.nombre = data_validada.get('nombre')
        conexion.session.commit()
        resultado = IngredienteResponseDTO().dump(ingrediente)
        return {
          'message': 'Ingrediente actualizado exitosamente',
          'content': resultado
        }
      else:
        return {
          'message':'ingrediente a actualizar no existe'
        }, 404
    except Exception as e:
      return {
        'message': 'Error al actualizar el ingrediente',
        'content': e.args
      },400
  
