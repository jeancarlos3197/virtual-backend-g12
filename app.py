from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def inicio():
  # render_template renderiza un archivo .html o .jinja para que flask lo pueda leer en interpretar al cliente
  return render_template('inicio.html', nombre='Jean Carlos', dia='Feliz jueves', edad=31, integrantes=['Foca','Lapagol','Ruidiaz','Paulin','Rayo Advincula'], usuario={'nombre':'Juan',
  'direccion':'Las piedristas 105',
  'edad':40},
  selecciones = [{
    'nombre':'Bolivia',
    'clasificado':False
  },{
    'nombre':'Brasil',
    'clasificado':True
  },{
    'nombre':'Chile',
    'clasificado':False
  },{
    'nombre':'Peru',
    'timado':True
  }])

if(__name__ == '__main__'):
  app.run(debug=True)