# las tablas que queremos crear, en python se representa por clases, y cada columna sera su atributo

from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
  # ahora esta clase tendra un comportamiento de modelo(tabla en la bd)
  # id seria considerada como una columna de mi modelo(tabla) ingrediente
  id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
  nombre = Column(type_=types.String(length=45), nullable=False, unique=True)

  __tablename__ = 'ingredientes'