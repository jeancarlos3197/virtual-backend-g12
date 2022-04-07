from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

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
  serializer_class = None