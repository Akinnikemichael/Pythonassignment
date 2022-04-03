from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def print_hello_world(request):
    return HttpResponse("<h2>Hello world</h2>",)

def print_json(request):
    return JsonResponse({"key": "value"})