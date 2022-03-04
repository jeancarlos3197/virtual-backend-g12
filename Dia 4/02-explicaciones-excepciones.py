productId=input('Ingresa el id del producto')

# iremos a la db y budcaremos ese producto
# 1, 2, 3, 4, 5, 6, 7, 8, 9
try:
  if(productId == '10'):
    # emitira un error manualmente
    # se utilizara para no continuar con el flujo normal del proyecto
    raise Exception('El producto no existe en la bd')
  # if validar la cantidad de productos
  # if validar la fecha de vencimiento
  # comenzare a crear mi metodo de pago
  # if validar que el cliente tenga saldo suficiente
  print('La pasarela de pagos concluyo exitosamente')
  print('La ejecución continuara... ') #mercado pago

except Exception as error:
  print('Ups algo salio mal con el producto a buscar, mensaje: ', error.args[0])
else:
  print('el producto encontrado es: ...')

print('Yo soy el final del programa')