from rest_framework.request import Request
from rest_framework.permissions import BasePermission, SAFE_METHODS

# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
class SoloAdminPuedeEscribir(BasePermission):
  message="Este usuario no tiene permisos"
  
  def has_permission(self, request: Request, view):

    print(request.user)
    print(request.user.nombre)
    print(request.user.rol)
    print(request.auth)
    print(SAFE_METHODS)
    print(type(view))

    if request.method in SAFE_METHODS:
      return True
    else:
      return request.user.rol == "ADMINISTRADOR"
    #retorna si el rol es administrador=True
    # return request.method in SAFE_METHODS and request.user.rol == 'ADMINISTRADOR'
class SoloMozoPuedeEscribir(BasePermission):
  def has_permission(self, request: Request, view):
      if request.method == SAFE_METHODS:
        return True
      else:
        return request.user.rol == 'MOZO'