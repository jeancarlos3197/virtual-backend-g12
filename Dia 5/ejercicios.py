# para evitar el salto de linea en una impresion de pantalla print() podemos declarar un parametro end=''
print('hola',end='*')
print('estos son los ejercicios')
# Escriba una funcion que le pida al usuario ingresar la altura y el ancho de un rectangulo y que lo dibuje usando *, ejemplo:
# altura: 5
# ancho: 4
# Resultado:
# ****
# ****
# ****
# ****
# ****
# dibujar_rectangulo()
def dibujar_rectangulo():
  altura=int(input('Ingrese la altura: '))
  ancho=int(input('ingrese el ancho: '))

  for i in range(altura):
    for j in range(ancho):
      print('*', end='')
    print('')
# dibujar_rectangulo()
# Escribir una funcion que nosotros le ingresemos el grosor de un octagono y que lo dibuje
# Ejemplo:
# Grosor: 5
#       *****
#      *******
#     *********
#    ***********
#   *************
#   *************
#   *************
#   *************
#   *************
#    ***********
#     *********
#      *******
#       *****
# dibujar_octagono()
def dibujar_octagono(grosor):
  pass

dibujar_octagono(5)
# Ingresar un numero entero y ese numero debe de llegar a 1 usando la serie de Collatz
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando el numero es 1
# Ejemplo 19
# 19 58 29 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
# serie_collatz()
series=[]
def serie_collatz(numero):
  if numero !=1:
    if numero%2==0:
      numero = numero//2
      series.append(numero)
    else:
      numero = (numero*3)+1
      series.append(numero)
    serie_collatz(numero)
  return series
# print(serie_collatz(50))
