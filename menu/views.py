from rest_framework.generics import CreateAPIView

from .models import Plato
from .serializers import PlatoSerializer
class PlatoCreateApiView(CreateAPIView):
  serializer_class = PlatoSerializer
  queryset = Plato.objects.all()
