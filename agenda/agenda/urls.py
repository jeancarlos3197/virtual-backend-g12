from django.contrib import admin
from django.urls import path, include
# include > incluye un archivo con varias rutas al archivo de rutas y solamente del proyecto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/', include('gestion.urls')),
]
