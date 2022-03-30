# librerias 
from datetime import timedelta
from flask import Flask, render_template
from flask_restful import Api
from os import environ
from dotenv import load_dotenv
from flask_cors import CORS
from flask_jwt import JWT, jwt_required, current_identity
from dtos.registro_dto import UsuarioResponseDTO

# archivos globales
from config import validador, conexion
from seguridad import autentificador, identificador
from seed import categoriaSeed

# carpetas
from controllers.usuarios import (  RegistroController, 
                                    LoginController,
                                    ResetPasswordController )
from controllers.movimientos import MovimientoController

load_dotenv()

app=Flask(__name__)
CORS(app=app)


app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
# para cambiar el endpoint de mi JWT
app.config['JWT_AUTH_URL_RULE'] = '/login-jwt'
# para cambiar la llave para solicitar el username
app.config['JWT_AUTH_USERNAME_KEY'] = 'correo'
# para cambiar la llave para solicitar el password
app.config['JWT_AUTH_PASSWORD_KEY'] = 'pass'
# para cambiar el tiempo de expiración de mi JWT
app.config['JWT_EXPIRATION_DELTA'] = timedelta(hours=1, minutes=5)
# 
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'

jsonwebtoken = JWT(app=app, authentication_handler=autentificador, identity_handler=identificador)

api = Api(app=app)
validador.init_app(app)
conexion.init_app(app)
conexion.create_all(app=app)

# ingresara antes de hacer el primer request a nuestra funcion toda la logica que queramos que se haga antes  de la primera solicitud la deberemos de colocar aqui
@app.before_first_request
def seed():
  # ahora hacemos el seed de las tablas respectivas
  categoriaSeed()


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

#al colocar jwt_required() estamos indicando que para ese controlador se debera de proveer una JWT valida
@app.route('/yo')
@jwt_required()
def perfil_usuario():
  print(current_identity)
  usuario = UsuarioResponseDTO().dump(current_identity)
  return {
    'message':'El usuario es',
    'content': usuario
  }

api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(MovimientoController, '/movimiento', '/movimientos')
api.add_resource(ResetPasswordController, '/reset-password')

if(__name__ == '__main__'):
  app.run(debug=True, port=8080)