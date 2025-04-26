from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello(request):
    return HttpResponse("Hello world")
