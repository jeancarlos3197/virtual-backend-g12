# un error es una mala ejecución del código que hará que mi proyecto o script deje de funcionar
# en python tenemos varios errores para los diferentes sucesos
# locals()['__builtins__'] me retornara del diccionario de locals() todos los errores definidos dentro de python y los atributos de los errores.
# dir> nos permite listar estos atributos como strings para poder leerlos facilmente
# locals()> nos devuelve todas las variables disponibles que tenemos en python en este scope
# print(dir(locals()['__builtins__']))

try:
  valor = int(input('Ingresa un numero: '))
  print(valor)
except:
  # capturara el error caustante impidiendo que el programa deje de funcionar 
  print('Algo salio mal intentalo nuevamente')

print('Yo finalizo correctamente')