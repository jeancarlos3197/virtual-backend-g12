# Colección de datos es una variable que puede almacenar  varios valores

# Lista(list)
# ordenadas y que puede ser modificadas

nombre=['Pedro','Luis','Danny','Cesar','Magaly','Anahi']

combinada=['Eduardo', 80, False, 15.8, [1,2,3]]

# Las listas siempre empiezan con la inicial 0
print(nombre[0])

# 
print(nombre[-1])
print(nombre)

# Si queremos ingresar a una posicion inexsistente nos lanzara error de 'indice fuera de rango'
# print(nombre[10])

# pop() > remueve el ultimo elemento de la lista y se puede almacenar en otra variable
resultado = nombre.pop()
print(resultado)
print(nombre)

# append() > ingresar un nuevo elemento a la ultima posición de la lista
nombre.append('Juana')

# elimina el contenido de una posición de la lista pero no lo podemos almacenar en otra variable
del nombre[0]

print(nombre)

# clear() > limpia toda la lista y la deja como nueva
nombre.clear()
print(nombre)

# indicar una sub selección de la lista
x = combinada[:] #.copy()
print(combinada[1:3])
print(id(x))
print(id(combinada))

# Indicando el contenido de la lista y esto es muy util para hacer una copia de la lista sin usar su misma posición de memoria
print(combinada[:])

meses_dscto = ['Enero','Marzp','Julio']
mes='Setiembre'
mes2='Enero'

# Indicara si el valor no se encuentra dentro de la lista
print(mes not in meses_dscto)

# indicar el valor si se encuentra en la lista
print(mes2 in meses_dscto)

seccion_a = ['Roxama','Juan']
seccion_b = ['Julieta','Martin']

# Si hacemos una sumatoria en las listas se combinara 

# Sirve para esperar un dato


# Tuplas
# muy similares a la lista a excepción que no se puede modificar
cursos=('backend','fronted',1,True)

print(cursos)
print(cursos[0])
print(cursos[0:2])

# cursos[0]='mobile design' No se podra agregar o modificar una tupla
# En la tupla solamente no podremos alterar los valores pertenecientes a ella pero si dentro de esta hay una lista u otra coleccion de datos que si se puede modificar entonces si podremos alterar esta subcolección sin problemas
variada=(1,2,3, [4,5,6])
variada[3][0] = 'Hola'

print(variada)

print(2 in variada)
# creamos una nueva lista a raiz de una tupla llamando a la clase list en la cual en el constructor de esa clase le pasos los valores que contendra la nueva lista
variada_lista=list(variada)
# no se puede crear una lista a raiz de otra lista eso lanzara un error , solo se puede crear una lista mediante su constructor mediante una tupla
list((1,2,3)) #[1,2,3]

print(variada_lista)

# para ver la cantidad de elementos que conforman una tupla o una lista
# Nota: la longitud siempre sera la cantidad de elementos y esta siempre empezara en 1 mientras que la posición siempre empezara en 0, es por eso que siempre longitud=posicion +1
print(len(variada))

# conjuntos( Set )
# Colección de datos DESORDENADA, una vez que se crea ya no se accede a las posiciones de sus elementos 
estaciones={'Verano','Otonio','Primavera','Invierno'}
# una vez que se crea se asigna una posicion  aleatoria pero no cambia cada vez que se manda llamar a este conjunto
print('Invierno' in estaciones)

# se agrega de forma aleatoria
estaciones.add('Otro')
# al ser desordenado al momento de retirar el ultimo elemento este sera completamente aleatorio y retirara el ultimo elemento agregado de forma aleatoria
# pop() quieta el ultimo elemento de la colección de datos (list, tuples, set)
estacion = estaciones.pop()
print(estacion)

#Diccionarios
# una coleccion de datos DESORDENADA pero cada elemento obedece a una llave definida
persona={
  'nombre': 'Jean',
  'apellido':'Garcia',
  'correo':'garcia.ademir.p@gmail.com'
}
# hacemos la busqueda de una determinada llave y si no la encuentra nos retornara opcionalmente None
print(persona.get('nombre','No existe'))
# devuelve todas las llaves de mi diccionario
print(persona.keys())
# devuelve todas los contenidos de mi diccionario
print(persona.values())
# devuelve todas las llaves y su contenido en forma de tuplas dentro de una lista
print(persona.items())
# si mandamos a llamar a una llave que no existe, la creara, caso contrario modificara su valor
persona['edad'] = 28
# Nota: si la llave no es exactamente igual creara una nueva (tiene que coincidir minus y mayus)
persona['Nombre'] = 'Ximena'
print(persona)

# eliminar una llave de un diccionario
persona.pop('apellido')