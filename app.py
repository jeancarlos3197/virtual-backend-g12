# librerias
from flask import Flask
from datetime import datetime
from flask_restful import Api

from controllers.ingredientes import IngredientesController

app = Flask(__name__)
# creamos la instancia de flask_restful.Api y le indicamos que todo la configuracion que haremos se agregue anuestra instancia de Flask
api = Api(app=app)

@app.route('/status', methods=['GET'])
def status():
  return {
    'status': True,
    'date': datetime.now().strftime('%Y-%M-%d %H:%M:%S')
  }

# Ahora definimos las rutas que van a ser utilizados con un determinado controlador
api.add_resource(IngredientesController,'/ingredientes','/ingrediente')

# comprueba que la instancia de la clase Flask se este ejecutando en el archivo principal del proyecto, esto se usa para no crear multiples instancias y generar un posible error de Flask
if __name__ == '__main__':
  app.run(debug=True)