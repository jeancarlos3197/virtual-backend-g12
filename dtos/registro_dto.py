from marshmallow import validate, fields
from marshmallow_sqlalchemy import auto_field

from config import validador

from models.usuarios import Usuario

# DTO > Data Transfery Object
class RegistroDTO(validador.SQLAlchemyAutoSchema):
  correo = auto_field(validate=validate.Email())
  class Meta:
    model = Usuario
  
class UsuarioResponseDTO(validador.SQLAlchemyAutoSchema):
  password = auto_field(load_only=True)
  class Meta:
    model = Usuario

# hacer un DTO que solamente reciba un correo y un password, el correo debe ser email, no es necesario usar un SQLAlchemyAutoSchema, solamente un validador.Schema
class LoginDTO(validador.Schema):
  correo = fields.Email(required=True)
  password = fields.String(required=True)