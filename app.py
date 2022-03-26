from flask import Flask, render_template
from flask_restful import Api
from os import environ
from dotenv import load_dotenv

from config import validador, conexion
from controllers.usuarios import RegistroController, LoginController

load_dotenv()

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)

conexion.create_all(app=app)

@app.route('/')
def inicio():
  # render_template renderiza un archivo .html o .jinja para que flask lo pueda leer en interpretar al cliente
  return render_template('inicio.html', nombre='Jean Carlos', dia='Feliz jueves', edad=31, integrantes=['Foca','Lapagol','Ruidiaz','Paulin','Rayo Advincula'], usuario={'nombre':'Juan',
  'direccion':'Las piedristas 105',
  'edad':40},
  selecciones = [{
    'nombre':'Bolivia',
    'clasificado':False
  },{
    'nombre':'Brasil',
    'clasificado':True
  },{
    'nombre':'Chile',
    'clasificado':False
  },{
    'nombre':'Peru',
    'timado':True
  }])

api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')

if(__name__ == '__main__'):
  app.run(debug=True, port=8080)