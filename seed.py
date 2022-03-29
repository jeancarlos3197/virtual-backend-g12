from config import conexion

from models.categorias import Categoria

# leer en la bd si no existe las categorias: 'OCIO', 'COMIDA', 'EDUCACION', 'VIAJES'

def categoriaSeed():
  # si existe las categorias ya no se ingresa 
  conexion.session.query(Categoria).filter(Categoria.nombre == 'OCIO', Categoria.nombre == 'COMIDA').first()
  pass