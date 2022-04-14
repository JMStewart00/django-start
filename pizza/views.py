from .models import *

from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import PizzaToppingSerializer, PizzaTypeSerializer

class PizzaToppingViewSet(viewsets.ModelViewSet):
  queryset = PizzaTopping.objects.all()
  serializer_class = PizzaToppingSerializer
  permission_classes = [IsAuthenticated]

class PizzaTypeViewSet(viewsets.ModelViewSet):
  queryset = PizzaType.objects.all()
  serializer_class = PizzaTypeSerializer
  permission_classes = [IsAuthenticated]
