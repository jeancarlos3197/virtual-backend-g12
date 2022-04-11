from django.urls import  path
from .views import (  inicio, 
                      PruebaApiView, 
                      TareasApiView,
                      TareaApiView,
                      EtiquetasApiView,
                      ArchivosApiView,
                      EliminarArchivoApiView)

urlpatterns = [
  path('inicio', inicio),
  path('prueba', PruebaApiView.as_view()),
  path('tareas', TareasApiView.as_view()),
  path('tarea/<int:pk>', TareaApiView.as_view()),
  path('etiquetas', EtiquetasApiView.as_view()),
  path('subir-imagen', ArchivosApiView.as_view()),
  path('eliminar-imagen', EliminarArchivoApiView.as_view()),
]