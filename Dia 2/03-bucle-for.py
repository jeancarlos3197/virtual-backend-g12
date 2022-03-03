# 
notas=[10,20,16,8,6,1]

# for(let i=0, i<10;i++){...}
# en cada iteracion de la lista notas tendremos su valor y lo almacenaremos en una variable llamada nota
# el mismo funcionamiento se da para cualquier colección de datos(lista, tupla, diccionario, conjunto)
for nota in notas:
  print(nota)

# Crearemos un bucle manual para una iteracion hasta el limite definido en el range
for numero in range(10):
  print(numero)

# si colocamos dos parametros el primero significara el numero inicial y el segundo el tope
for numero in range(5,10):
  print(numero)

# si colocamos tres parametros el primero significara el numero inicial, el segundo el tope y el tercero sera de cuanto a cuanto hara la incrementacion o decrementacion
# empezara en 5, hasta <10 y en cada ciclo incrementara en 2 unidades
for numero in range(5,10,2):
  print(numero)



