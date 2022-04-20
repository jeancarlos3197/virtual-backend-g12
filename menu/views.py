from django.utils import timezone
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.permissions import (  AllowAny, 
                                          IsAuthenticated, 
                                          IsAdminUser, 
                                          IsAuthenticatedOrReadOnly,
                                        )
from rest_framework.request import Request
from rest_framework.response import Response
from cloudinary import CloudinaryImage

from .models import Plato, Stock
from .serializers import (  AgregarDetallePedidoSerializer, PedidosSerializer, 
                            PlatoSerializer, 
                            StockSerializer, )
from .permissions import SoloAdminPuedeEscribir, SoloMozoPuedeEscribir
from fact_electr.models import Pedido, DetallePedido

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

class StockApiView(ListCreateAPIView):
  serializer_class= StockSerializer
  queryset=Stock.objects.all()
  permission_classes = [IsAuthenticated, SoloAdminPuedeEscribir]

class PedidoApiView(ListCreateAPIView):
  queryset = Pedido.objects.all()
  serializer_class = PedidosSerializer
  permission_classes = [IsAuthenticated, SoloMozoPuedeEscribir]
  
  def post(self, request: Request):
    print(request.user)
    # Le agrego al body el usuarioId proveniente de la autenticación de la token
    request.data['usuarioId'] = request.user.id
    data = self.serializer_class(data=request.data)
    data.is_valid(raise_exception=True)
    data.save()
    return Response(data=data.data, status=status.HTTP_201_CREATED)

class AgregarDetallePedidoApiView(CreateAPIView):
  queryset = DetallePedido.objects.all()
  serializer_class = AgregarDetallePedidoSerializer
  def post(self, request: Request):
    # VALIDA la data con elserializer
    data=self.serializer_class(data=request.data)
    data.is_valid(raise_exception=True)
    # SELECT * FROM stocks WHERE fecha='...' AND plato_id= '...';
    stock = Stock.objects.filter(fecha=timezone.now(), platoId=data.validated_data.get('platoId')).first()
    print(stock)
    # verifico que tenga esa cantidad de productos en stock
    # {
        # "cantidad":2,
        # "plato":1,
        # "pedido_id": 2
    # }
    # agrego el detalle
    return Response(data={'message':'Detalle agregado exitosamente'})