import unittest

def numero_par(numero):
  # retornara verdadero si es par o false si es impar
  return numero % 2 == 0

# todo escenario de testing sera basado en clases
class Prueba(unittest.TestCase):
  # testCase me permite hacer varios tipos de comparaciones y ademas le indicara a python que clase de testing debe hacer

  # cada escenario de prueba sera un metodo
  def test_sumatoria(self):
    numero1 = 1
    numero2 = 2
    resultado = numero1 + numero2
    # comparar si numero1 + numero2 es igual a 3
    self.assertEqual(resultado, 3)

  # si estamos concientes que el test va a fallar pero aun asi queremos mantenerlo tal y como esta, entonces podemos usar el decorador expectedFailure que no nos indicara un fallo pero se espera el fallo
  @unittest.expectedFailure
  def test_resta(self):
    numero1 = 1
    numero2 = 2
    resultado = numero1 - numero2
    # comparar si numero1 + numero2 es igual a 3
    self.assertEqual(resultado, 3)

class NumeroParTest(unittest.TestCase):
  def test_par(self):
    '''Deberia retornar True si el numero es par'''
    resultado = numero_par(2)
    self.assertEqual(resultado, True)

  def test_impar(self):
    '''Deberia retornar False si el numero es impar'''
    resultado = numero_par(3)
    self.assertEqual(resultado, False)

  def test_no_funciona(self):
    '''Debera arrojar un error si se le pasa una letra en vez de un numero'''
    # si se que el siguiente test fallara pero es parte del caso entonces puedo usar el assertRaises para que python me avise que el test fallo y recibira el tipo de error que va a generar para poder testearlo
    with self.assertRaises(TypeError, msg='Error al ingresar un caracter en vez de un numero') as error:
      numero_par('a')
    self.assertEqual(error.msg, 'Error al ingresar un caracter en vez de un numero')