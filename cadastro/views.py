from django.http import HttpResponse
from django.shortcuts import render

from cadastro.models import Curso


# Create your views here.


def index(request):
    return HttpResponse("Olá, Mundo! Agora estou na web")


def teste(request):
    return HttpResponse("Isso é um teste.")

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "listar_cursos.html", {'lista':cursos})