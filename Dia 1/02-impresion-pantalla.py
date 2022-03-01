nombre = 'jean'

print(nombre)
#concatenar (juntar) varios valores
print('El nombre es:', nombre,'del usuario')

estado_civil = 'viudo'

# Si queremos usar el metodo format debemos coincidir el mismo numero de veces que colocamos {} con la cantidad de variables
print('La persona {} es {}'.format(nombre, estado_civil))

# ademas podemos agregar la posición de la variable que  queremos imprimir dentro de las llaves
print('{1} es una persona {0}'.format(estado_civil, nombre))