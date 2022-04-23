from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import GenerarComprobanteSerializer, ComprobanteSerializer
from .generar_comprobante import generar_comprobante

class GenerarComprobanteApiView(CreateAPIView):
  serializer_class = GenerarComprobanteSerializer
  def post(self, request):
    data = self.serializer_class(data=request.data)

    data.is_valid(raise_exception=True)
    try:
      comprobante = generar_comprobante(**data.validated_data)
      respuesta = ComprobanteSerializer(instance=comprobante)
  
      return Response(data={'message': 'Comprobante creado exitosamente', 'content': respuesta.data}, status=status.HTTP_201_CREATED)

    except Exception as e:
      return Response(data={'message':'Error al crear el comprobante', 'content': e.args}, status=status.HTTP_400_BAD_REQUEST)

