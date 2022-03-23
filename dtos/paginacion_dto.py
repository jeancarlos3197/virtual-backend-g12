from marshmallow import fields

from config import validador


class PaginacionRequestDTO(validador.Schema):
  page = fields.Integer(required=False, load_default=1)
  perPage = fields.Integer(required=False, load_default=10)