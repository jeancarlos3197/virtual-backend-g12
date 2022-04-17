from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import (  AllowAny, 
                                          IsAuthenticated, 
                                          IsAdminUser, 
                                          IsAuthenticatedOrReadOnly,
                                        )
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from cloudinary import CloudinaryImage

from .models import Plato
from .serializers import PlatoSerializer

class PlatoApiView(ListCreateAPIView):
  serializer_class = PlatoSerializer
  queryset = Plato.objects.all()
  permission_classes = [IsAuthenticatedOrReadOnly]

  def get(self, request:Request):
    data = self.serializer_class(instance=self.get_queryset(), many=True)
    print(data)
    #Hacer una iteracion para modificar la foto de cada plato y devolver el link de la foto
    print(data.data[0].get('foto'))
    link = CloudinaryImage('plato/ngwiew7pvnwbmcyhbe35.jpg').image(secure=True)

    print(link)
    return Response(data={
      'status': data.data,
    }, status=status.HTTP_200_OK)