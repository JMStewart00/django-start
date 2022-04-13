from django.contrib import admin
from .models import Pizza, PizzaType, PizzaTopping, ProperOrder

# Register your models here.
admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(PizzaType)
admin.site.register(ProperOrder)