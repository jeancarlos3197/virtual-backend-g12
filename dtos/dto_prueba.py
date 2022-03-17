from config import validador
from marshmallow import fields, validate

class ValidadorPrueba(validador.Schema):
  nombre = fields.Str(validate=validate.Length(max=10))
  apellido = fields.Str()
  edad = fields.Int()
  soltero = fields.Bool()

  # class Meta:
    # es una clase que va a ser para poder pasar parametros a la metadata del padre (de la clase de la cual estamos heredando), definimos atributos que van a ser a la clase Schema para poder hacer la validacion correcta
    # en el atributo fieldsiran lo que seria que valores necesitamos esperar del cliente
    # fields = ['nombre', 'apellido']

class ValidadorUsuarioPrueba(validador.Schema):
  nombre = fields.Str()
  apellido = fields.Str()