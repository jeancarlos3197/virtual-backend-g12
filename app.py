# librerias
from flask import Flask
from datetime import datetime
from flask_restful import Api

from controllers.ingredientes import IngredientesController, PruebaController
from config import conexion, validador


app = Flask(__name__)
# creamos la instancia de flask_restful.Api y le indicamos que todo la configuracion que haremos se agregue anuestra instancia de Flask
api = Api(app=app)

# aca se almacenara todas las variables de configuracion de mi proyecto Flask, en ella se podran encontrar algunas variables como DEBUG y ENV, entre otras.
# app.config es un diccionario en el cual se almacena las variables por Llave. Valor
# print(app.config)

# Ahora asignaremos la cadena de conexion a nuestra base de datos
#                                  tipo://usuario:password@dominio:puerto/base_de_datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Aa123@127.0.0.1:3306/recetario'
# Si se establece True entonces SQLALCHEMY rastreara las modificaciones de los objectos (modelos) y emitira señales cuando cambie algun modelo, su valor por defecto es None
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# para jalar la configuracion de mi flask y extraer su conexion a la base de datos
conexion.init_app(app)
# para jalar la configuracion de mi flask y poder 
validador.init_app(app)

# con el sgt comando indicaremos la creacion de todas las tablas en bd
# emitira unerror si es que no hay ninguna tabla a crear
# emitira unerror si no le hemos instalado el conector correctamente
conexion.create_all(app=app)

@app.route('/')
def inicio():
  return 'Bienvenido a mi API de recetas'

@app.route('/status', methods=['GET'])
def status():
  return {
    'status': True,
    'date': datetime.now().strftime('%Y-%M-%d %H:%M:%S')
  }

# Ahora definimos las rutas que van a ser utilizados con un determinado controlador
api.add_resource(IngredientesController,'/ingredientes','/ingrediente')
api.add_resource(PruebaController,'/pruebas')

# comprueba que la instancia de la clase Flask se este ejecutando en el archivo principal del proyecto, esto se usa para no crear multiples instancias y generar un posible error de Flask
if __name__ == '__main__':
  app.run(debug=True)