from rest_framework.request import Request
from rest_framework.permissions import BasePermission

# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
class SoloAdminPuedeEscribir(BasePermission):
  def has_permission(self, request: Request, view):

    print(request.user)
    return True