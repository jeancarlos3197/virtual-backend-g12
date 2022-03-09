from datetime import datetime
from flask import Flask, request

app = Flask(__name__)

clientes=[]

@app.route('/')
def estado():
  hora_del_servidor = datetime.now()

  return{
    'status':True,
    'hour':hora_del_servidor.strftime('%d/%m/%Y %H:%M:%S')
  }

@app.route('/clientes', methods=['POST'])
def obtener_clientes():
  # solamente puede ser llamado en cada controlador (funcion que se ejecutara cunado se realice una peticion desde el front)
  print(request.method)
  # request.method. mostrara el tipo de estado que se esta ejecutando
  print(request.get_json())
  data = request.get_json()
  clientes.append(data)
  return {
    'message':'Cliente agregado exitosamente',
    'client':data
  }

app.run(debug=True)