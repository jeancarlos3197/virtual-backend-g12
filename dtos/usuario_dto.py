from marshmallow import fields

from config import validador

class ResetPasswordRequestDTO(validador.Schema):
  correo = fields.Email()