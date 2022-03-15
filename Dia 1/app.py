from datetime import datetime
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
# si solamente mandamos a llamar a la clase y le pasamos la instancia de la clase flask creara los permisos para que todos puedan acceder (Allowed-Origin), para que cualquier metodo pueda ser consultada (Allow-Method) y para cualquier header ( Allowed-Header)
CORS(app=app, origins=['http://127.0.0.1:5500'], methods='*', allow_headers=['Content-Type'])

clientes=[
  {
    "nombre": "Jean Carlos",
    "pais": "PERU",
    "edad": 29,
    "id":1,
    "organos": True,
    "casado": False
  },
]

@app.route('/')
def estado():
  hora_del_servidor = datetime.now()

  return{
    'status':True,
    'hour':hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S')
  }

@app.route('/clientes', methods=['POST','GET'])
def obtener_clientes():
  # solamente puede ser llamado en cada controlador (funcion que se ejecutara cunado se realice una peticion desde el front)
  print(request.method)
  # request.method. mostrara el tipo de estado que se esta ejecutando
  print(request.get_json())
  if request.method == 'POST':
    data = request.get_json()
    # data # agregar una llave llamada id que sera la longitud de la lista actual +1 
    # data['id']='...'
    data['id'] = len(clientes)+1
    clientes.append(data)
    return {
      'message':'Cliente agregado exitosamente',
      'client':data
    }

  elif request.method == 'GET':
    # Ingreseara cuando el metodo sea GET
    return {
      'message':'La lista de clientes',
      'clients':clientes
    }

@app.route('/cliente/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def gestion_usuario(id):
  print(id)
  if request.method == 'GET':
    # iterar la lista y buscaremos el cliente por ese id y si no existe imprimir un mensaje
    usuario = buscar_cliente(id)
    if usuario:
      return usuario[0]
    else:
      return {
        'message':'el usuario a encontrar no se encontro'
      },404

  elif request.method == 'PUT':
    resultado = buscar_cliente(id)
    if resultado:
      # hacemos la destructuracion de nuestra tupla creando las variables cliente y posicion
      [cliente, posicion] = resultado
      # resultado[0] > cliente
      # resultado[1] > posicion
      # modificar el cliente
      # extraemos la informacion del body y la almacenamos en una variable
      data = request.get_json()
      # en ese diccionario agregaremos una llave 'id' y almacenaremos el id del cliente que esta en la posicion 0 de la tupla del cliente encontrado
      data['id'] = id
      # extraemos la posicion del cliente devuelta en la posicion 1 de la tupla de buscar_cliente
      # posicion = resultado[1]
      # modificar ese cliente con el nuevo valor
      clientes[posicion] = data
      return data
    else:
      return {
        'message':'El usuario a modificar no se encontro'
      },404

  elif request.method == 'DELETE':
    # eliminar ese cliente luego de validar si existe o no usando el metodo validar_usuario(id) si no existe indicar lo mismo 'cliente a eliminar no se encuentre
    resultado = buscar_cliente(id)
    if resultado:
      [cliente, posicion] = resultado
      cliente_eliminado = clientes.pop(posicion)
      return{
        'message':'cliente eliminado exitosamente',
        'cliente': cliente_eliminado
      }
    else:
      return{
        'message': 'El cliente a eliminar no se encontro'
      },404

def buscar_cliente(id):
  # for cliente in clientes:
  #   if cliente.get('id') == id:
  #     return cliente
  for posicion in range(0, len(clientes)):
    cliente= clientes[posicion]
    if cliente.get('id') == id:
      return (cliente, posicion)

app.run(debug=True)