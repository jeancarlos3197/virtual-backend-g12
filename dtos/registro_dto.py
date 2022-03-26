from config import validador
from models.usuarios import Usuario

# DTO > Data Transfery Object
class RegistroDTO(validador.SQLAlchemyAutoSchema):
  class Meta:
    model = Usuario
  


    