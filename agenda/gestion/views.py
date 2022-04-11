# https://www.django-rest-framework.org/api-guide/status-codes/#status-codes
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ( ListAPIView, 
                                      ListCreateAPIView, 
                                      RetrieveUpdateDestroyAPIView,
                                      CreateAPIView,
                                      DestroyAPIView, )
# son un conjunto de librerias que django nos provee para poder utilizar de una manera mas rapida ciertas configuraciones, timezone sirve para en base a la configuracion que colocamos en el settings.py TIME_ZONE se basata en esta para darnos a hora y fecha con esa configuracion
from django.utils import timezone
# https://docs.djangoproject.com/es/4.0/_modules/django/core/files/uploadedfile/
from django.core.files.uploadedfile import InMemoryUploadedFile
# https://docs.djangoproject.com/en/4.0/topics/files/#storage-objects
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from os import remove

from .serializers import (  PruebaSerializer, 
                            TareasSerializer,
                            TareaSerializer,
                            TareaPersonalizableSerializer,
                            EtiquetaSerializer,
                            ArchivoSerializer,
                            EliminarArchivoSerializer,)
from .models import Tareas, Etiqueta

# https://www.django-rest-framework.org/api-guide/requests/
@api_view(http_method_names=['GET', 'POST'])
def inicio(request: Request):
  # request sera toda la informacion enviada por el cliente
  if request.method == 'GET':
    return Response(data= {
      'message': 'Hiciste una peticion GET'
    }, status=200)

  elif request.method == 'POST':
    return Response(data= {
      'message': 'Hiciste una peticion POST'
    }, status=201)

class PruebaApiView(ListAPIView):
  # sirve para ayudarnos a cuando se llame este request nos hara el trabajo de serializer y de deserializar la informacion (es igual a un DTO)
  serializer_class = PruebaSerializer
  # queryset > encargado de hacer la busqueda para este controlador (para todos sus metodos)
  queryset = [{
    'nombre':'Jean Carlos', 
    'apellido': 'Garcia', 
    'correo': 'jean@gmail.com', 
    'dni': '12345678',
    'estado_civil': 'soltero'},
    {
    'nombre':'Jean Carlos', 
    'apellido': 'Garcia', 
    'correo': 'jean@gmail.com', 
    'dni': '12345678',
    'estado_civil': 'soltero'}]

  def get(self, request: Request):
    # dentro de las vistas genericas se puede sobre escirbir la logica inicial del controlador
    # si modifico la logica original de cualquier generico en base a su metodo a utilizar ya no esra necesario definir los tributos serializer_class y queryset ya que estas se usan para cuando no se modifica la logica original
    informacion = self.queryset
    # Uso el serializador para filtar la informacion necesaria y no mostrar alguna informacion de mas pero en este caso como le voy a pasar uno o mas registros de usuario entonces para que el serializador los pueda iterar le coloco el parametro many=True que lo que hara sera iterar
    informacion_serializada = self.serializer_class(data=informacion, many=True)
    # para utilizar la informacion serializada OBLIGATORIAMENTE tengo que llamar al metodo is_valid() el cual internamente hara la validacion de los campos y sus configuraciones
    # el parametro raise_exception hara la emision del error si es que hay indicando cual es el error
    informacion_serializada.is_valid(raise_exception=True)
    # print(informacion)
    return Response(data={
      'message': 'Hiciste una peticion GET',
      'content': informacion_serializada.data
    })

class TareasApiView(ListCreateAPIView):
  queryset = Tareas.objects.all()
  serializer_class = TareasSerializer

  def post(self, request:Request):
    # serializo la data para validar sus valores y su configuracion
    serializador = self.serializer_class(data=request.data)
    # llamo al metodo validar que retornara True si cumple o False si no
    if serializador.is_valid():
      # serializador.initial_data > data inicial sin la validacion
      # serializador.validated_data > data ya validada (solo se puede llamar luego de llamar al metodo is_valid())
      # validare que la fecha_caducidad no sea menor que hoy
      fechaCaducidad = serializador.validated_data.get('fechaCaducidad')
      print(serializador.validated_data.get('fechaCaducidad'))
      # validar que la importancia sea entre 0 y 10
      importancia = serializador.validated_data.get('importancia')

      if  importancia < 0 or importancia > 10:
        return Response(data= {
          'message': 'La importancia debe estar entre 0 y 10'
        }, status=status.HTTP_400_BAD_REQUEST)

      if timezone.now() > fechaCaducidad:
        return Response(data={
          'message': 'La fecha de caducidad no puede ser menor que la fecha actual'
        }, status=status.HTTP_400_BAD_REQUEST)
      
      # el metodo save() se podra llamar siempre que el serializado sea un ModelSerializer y este servira para poder guardar la informaacion actual del serializador en la bd
      serializador.save()
      return Response(data=serializador.data, status=status.HTTP_201_CREATED)
    else:
      # mostrara todos los errores que hicieron que el is_valid() no cumpla la condicion 
      # serializador.errors
      return Response(data={
        'message': 'La data no es valida',
        'content': serializador.errors}, 
        status=status.HTTP_400_BAD_REQUEST)

class EtiquetasApiView(ListCreateAPIView):
  queryset= Etiqueta.objects.all()
  serializer_class = EtiquetaSerializer

class TareaApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = TareaSerializer #TareaPersonalizableSerializer
  queryset = Tareas.objects.all()

class ArchivosApiView(CreateAPIView):
  serializer_class= ArchivoSerializer
  def post(self, request:Request):
    data = self.serializer_class(data=request.FILES)

    query_params = request.query_params
    carpetaDestino = query_params.get('carpeta')

    if data.is_valid():
      print(data.validated_data.get('archivo'))
      archivo: InMemoryUploadedFile = data.validated_data.get('archivo')
      print(archivo.name)
      if archivo.size > (5 * 1024 * 1024):
        return Response( data={
          'message': 'Archivo muy grande, no puede ser mas de 5Mb'
        }, status=status.HTTP_406_NOT_ACCEPTABLE) 
      # el metodo read() sirve para leer el archivo PEERO la lectura la lectura hara que tambien se elimine de la memoria tempoeral por ende no se puede llamar dos o mas veces a este metodo ya que la segunda ya no lo tendremos archivo que mostrar
      resultado = default_storage.save(
        # usar operador ternario para que si es que la carpetaDestino no es None ponerla caso contrario poner ''
        (carpetaDestino+'/' if carpetaDestino is not None else '') +
        archivo.name, ContentFile(archivo.read()))
      print(resultado)
      return Response(data={
        'message': 'Archivo guardado exitosamente',
        'content':{
          'ubicacion': resultado
        }
        }, status=status.HTTP_201_CREATED)
    else:
      return Response(data={
        'message': 'Error al subir la imagen',
        'content': data.errors
      }, status=status.HTTP_400_BAD_REQUEST)

class EliminarArchivoApiView(DestroyAPIView):
  # El generico DestroyApiView solicita una pk como parametro de la url para eliminar un determinado registro de un modelo pero se personalizara para no recibir ello
  serializer_class = EliminarArchivoSerializer

  def delete(self, request:Request):
    data = self.serializer_class(data=request.data)
    
    try:
      if data.is_valid():
        ubicacion = data.validated_data.get('archivo')
        remove(settings.MEDIA_ROOT / ubicacion)
        return Response(data={
          'message': 'Archivo eliminado exitosamente',
        })
      else:
        return Response(data={
          'message':'Error al eliminar el archivo',
          'content':data.errors
        })
    except Exception as e:
      return Response(data={
        'message':'No se encontro el archivo a eliminar',
        'content':e.args
      }, status=status.HTTP_404_NOT_FOUND)
