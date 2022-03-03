# IF- ELSE
# python al no utilizar las llaves para definir bloque de un comportamiento diferente tenemos que utilizar tabulaciones(TAB)
from sre_constants import IN


edad= int(input('Ingresa tu edad: '))
if (edad > 18):
  # todo lo que escriba acá dentro
  print('la persona es mayor de edad')
  # la alineación nunca debe de variar si estamos en el mismo bloque de codigo
# se utiliza  si la primera condicion falla pero queremos hacer una segunda condicion
elif edad >15:
  print('Puedes ingresar a la preparatoria')
elif edad >10:
  print('Puedes vacunarte')
# el else es completamente opcional y no siempre se debe utilizar con un if
else:
  #todo lo demas
  print('La persona es menor de edad')
  # pass
print('finalizo el programa')

# validar si un numero ingresado por teclado es:
# mayor a 500: indicar que no recibe el bono yanapay
# entre 500 y 250 indicar que si  recibe el bono 
# es menor que 250: indicar que recibe el bono y un balon de gas
# RESOLUCIÓN DEL EJERCICIO

ingresos = int(input('Ingrese su ingreso: '))

if ingresos > 500:
  print('no recibe bono yanapay')
elif ingresos >= 250 and ingresos <= 500:
  print('Recibe bono')
else:
  print('Recibe bono y balon de gas')