from django.urls import path

from .views import json, single_topping

urlpatterns = [
    path("api/json", json, name="index"),
    path("api/json/<int:id>", single_topping),
]
