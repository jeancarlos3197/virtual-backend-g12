# las tablas que queremos crear, en python se representa por clases, y cada columna sera su atributo

from config import conexion
from sqlalchemy import Column, types

class Ingrediente(conexion.Model):
  # ahora esta clase tendra un comportamiento de modelo(tabla en la bd)
  # id seria considerada como una columna de mi modelo(tabla) ingrediente
  id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
  nombre = Column(type_=types.String(length=45), nullable=False, unique=True)

  # indicara cual es el nombre de la tabla en la base de datos, si no le ponemos o no definimos este atributo entonces será el nombre de la clase
  __tablename__ = 'ingredientes'