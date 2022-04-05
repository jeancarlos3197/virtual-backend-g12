from marshmallow import fields

from config import validador

class ResetPasswordRequestDTO(validador.Schema):
  correo = fields.Email()

class ChangePassworRequestDTO(validador.Schema):
  correo = fields.Email()
  new_password = fields.String()