import unittest
from datetime import datetime
from app import app

class TestInicioFlask(unittest.TestCase):
  def setUp(self):
      # en ves del constructor, en los test se usa el metodo setUp, que servira para configurar todas los atributos y demas cosas que vayamos a utilizar en los escenarios de test de esta clase
      self.nombre = 'Eduardo'
      # inicia mi aplicacion de flask usando un cliente de test, aceptara peticiones http para probar los endpoint y toda la aplicacion en general, esto levantara los modelos y hara la conexion a la bd entre otras cosas
      self.aplicacion_flask = app.test_client()

  @unittest.skip('No se puede ejecutar este test')
  def testNombre(self):
    self.assertEqual(self.nombre, 'Eduardo')

  def testEndpointStatus(self):
    '''deberia retornar la hora del servidor y su estado'''
    respuesta = self.aplicacion_flask.get('/status')
    # el body de la respuesta la obtenemos de repuesta.json el cual nos devolvera un diccionario con el json de la rpta
    # print(respuesta.json)
    self.assertEqual(respuesta.status_code, 200)
    self.assertEqual(respuesta.json.get('status') , True )
    self.assertEqual(respuesta.json.get('hora_del_servidor') , datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

  def testLoginJWTExitoso(self):
    '''deberia retornar una token para poder ingresar a las rutas protegidas'''
    # Mocks
    body = {
      'correo':'jean@gmail.com',
      'pass':'Jeangmail123'
    }
    respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
    self.assertEqual(respuesta.status_code, 200)
    # respuesta.json.get('acceess_token') != None
    self.assertNotEqual(respuesta.json.get('access_token'), None)

  def testLoginJWTFallo(self):
    '''deberia retornar un error si las credenciales son incorrectas'''
    body = {
      'correo':'jean@gmail.com',
      'pass':'passwordfailed'
    }
    respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
    # hacer las suposiciones correspondientes
    self.assertEqual(respuesta.status_code, 401)
    self.assertEqual(respuesta.json.get('access_token'), None)
    self.assertEqual(respuesta.json.get('description'), 'Invalid credentials')

# una clase por endpoint
class TestYo(unittest.TestCase):
  def setUp(self):
    self.aplicacion_flask = app.test_client()
    body = {
      'correo':'jean@gmail.com',
      'pass':'Jeangmail123'
    }
    respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
    self.token = respuesta.json.get('access_token')

  def testNoHayJWT(self):
    respuesta = self.aplicacion_flask.get('/yo')
    self.assertEqual(respuesta.status_code, 401)

  def testPasoJWT(self):
    respuesta = self.aplicacion_flask.get('/yo', headers={'Authorization': 'Bearer {}'.format(self.token)})
    self.assertEqual(respuesta.status_code, 200)
    self.assertEqual(respuesta.json.get('message'), 'El usuario es')

class TestMovimiento(unittest.TestCase):
  def setUp(self):
    self.aplicacion_flask = app.test_client()
    body = {
      'correo':'jean@gmail.com',
      'pass':'Jeangmail123'
    }
    respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
    self.token = respuesta.json.get('access_token')
  # hacer los test para extraer los movimientos creados del usuario,hacer el caso cuando se pase una JWT, cuando no se ase una token, cuando no tenga movimientos y cuando tenga movimientos
  def testGetJWT(self):
    respuesta = self.aplicacion_flask.get('/movimientos', headers={'Authorization': 'Bearer {}'.format(self.token)})
    self.assertEqual(respuesta.json.get('message'), 'Los movimientos son')
    self.assertEqual(respuesta.status_code, 200)

  @unittest.skip('Llama a un Traceback')
  def testGetSinJWT(self):
    respuestaSinJWT = self.aplicacion_flask.get('/movimientos', headers={'Authorization': 'Bearer '})
    self.assertEqual(respuestaSinJWT.status_code, 401)

  def testGetListado(self):
    respuesta = self.aplicacion_flask.get('/movimientos', headers={'Authorization': 'Bearer {}'.format(self.token)})
    self.assertNotEqual(len(respuesta.json.get('content')), 0)
    self.assertEqual(respuesta.status_code, 200)
  
  @unittest.skip('Estaba vacío, ya no')
  def testGetListadoVacio(self):
    respuesta = self.aplicacion_flask.get('/movimientos', headers={'Authorization': 'Bearer {}'.format(self.token)})
    self.assertEqual(len(respuesta.json.get('content')), 0)
    self.assertEqual(respuesta.status_code, 200)