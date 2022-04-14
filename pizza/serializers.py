from .models import PizzaTopping, PizzaType
from rest_framework import serializers

class PizzaToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaTopping
        fields = '__all__'

class PizzaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaType
        fields = '__all__'