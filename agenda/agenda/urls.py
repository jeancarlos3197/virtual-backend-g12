from django.contrib import admin
from django.urls import path, include
# include > incluye un archivo con varias rutas al archivo de rutas y solamente del proyecto
from django.conf.urls.static import static
from django.conf import settings
# SE PUEDE utilizar todas las variables definidas en el archivo SETTINGS del proyecto
urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# metodo statuc sirve para retornar una lista de URLPARTTERNS pero que establecera que archivos y que rutas retornara