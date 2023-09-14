from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Olá, Mundo! Agora estou na web")


def teste(request):
    return HttpResponse("Isso é um teste")