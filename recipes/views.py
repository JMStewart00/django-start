from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    json = {
        'key1': 'value1',
        'key2': 'value2',
    }
    return JsonResponse(json)

def second_index(request):
    return HttpResponse("Hello, world. You're at the recipes SECOND INDEX.")