from .models import *

from rest_framework import viewsets
from .serializers import PizzaToppingSerializer, PizzaTypeSerializer

class PizzaToppingViewSet(viewsets.ModelViewSet):
  queryset = PizzaTopping.objects.all()
  serializer_class = PizzaToppingSerializer

class PizzaTypeViewSet(viewsets.ModelViewSet):
  queryset = PizzaType.objects.all()
  serializer_class = PizzaTypeSerializer
