from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def json(request):
  data = {}
  # Query the database here
  # objects.all()
  # Returns queryset of dictionaries
  pizza_types_values = PizzaType.objects.all().values()

  # turn QuerySet into list
  # data['key'] = value
  data['pizza_types'] = list(pizza_types_values)

  # Query the database for all pizza toppings
  pizza_toppings_values = PizzaTopping.objects.all().values()
  # Add to the data dictionary
  data['pizza_toppings'] = list(pizza_toppings_values)

  # send data to frontend
  return JsonResponse(data)

def single_topping(request, id):
  # return single topping
  # we need to query again
  # id = request.GET.get('id')

  pt = PizzaTopping.objects.filter(id=id).values()
  data = list(pt)
  return JsonResponse(data[0])
  # return single topping
  # return JsonResponse(data)

# function to return json response
# query the database
# turn QuerySet into list
# get only the values, not instances
# send data to frontend with a return JsonResponse
# double check that I have a route for that view in urls.py
