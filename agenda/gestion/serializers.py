from dataclasses import fields
from rest_framework import serializers
from .models import Tareas, Etiqueta
# https://www.django-rest-framework.org/api-guide/serializers/
# https://www.django-rest-framework.org/api-guide/fields/
class PruebaSerializer(serializers.Serializer):
  nombre = serializers.CharField(max_length=40, trim_whitespace=True)
  apellido = serializers.CharField()
  correo = serializers.EmailField()
  dni = serializers.RegexField(max_length=8, min_length=8, regex='[0-9]{8}')
  # dni = serializers.IntegerField(min_value=1000000, max_value=99999999)

# https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
class TareasSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Tareas
    fields = '__all__' #estara indicando que columnas va a utilizar __all__ para usar todas
    # exclude = ['importancia'] #indicara que columnas no va a utilizar
    # Nota, no se puede usar los dos a la vez, fields o exclude
    extra_kwargs={
      'etiquetas': {
        'write_only': True,
      }
    }
    # depth = 1 # Sirve para que en el caso que querramos devolver la informacion de una relacion entre este modelo podemos indicar hasta que grado de profundidad queremos que nos devuelva la informacion, la profundida maxima es de 10

class TareaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tareas
    fields = '__all__'
    depth = 1

class TareaPersonalizableSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tareas
    fields = '__all__'
    #exclude = ['nombre'] #funcionara tanto para ectura como escritura
    extra_kwargs = {
      'nombre': {
        'read_only': True,
      }
    }

class EtiquetaSerializer(serializers.ModelSerializer):
  # indicara que este atributo solamente funcionara para cuando vamos a serializar la data ante de devolverlo mas no para cuando queremos para la escritura
  # se tiene que llamar igual que el related_name para poder ingresar a ese nombre del related_name
  # Nota: no podemos utilizar el parametro source si es que tbn colocaremos el mismo valor como nombre del atributo
  tareas = TareasSerializer(many=True, read_only=True)
  class Meta:
    model = Etiqueta
    fields = '__all__'
    # ¿Como puedo mediante un serializador indicar que columnas de determinado modelo seran solamente escritura o solamente lectura sin modificar su comportamiento como atributo de la clase?
    # extra_kwargs y read_only_fields solamente funcionaran para cuando nosotros querramos modificar el comportamiento de los atributos que no los hemos modificado manualmente dentro del serializador 
    extra_kwargs = {
      'nombre':{
        'write_only':True
        },
      'id':{
        'read_only':True
      }
    }
    # los campos del modelo que solamente quiero que sean lectura los padre definir en una lista
    read_only_fields = ['createdAt']


    