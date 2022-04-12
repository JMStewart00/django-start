from django.urls import path

from .views import index, second_index

urlpatterns = [
    path('', index),
    path('2', second_index),
]