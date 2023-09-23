from django.http import HttpResponse
from django.shortcuts import render, redirect

from cadastro.forms import CursoForm
from cadastro.models import Curso


# Create your views here.


def index(request):
    # return HttpResponse("Olá, Mundo! Agora estou na web")
    return render(request, "inicio.html")


def teste(request):
    return HttpResponse("Isso é um teste.")

def print_em_html(request):
    return HttpResponse("<h2>Um título</h2>")

def listarCursos(request):
    cursos = Curso.objects.all().order_by('nome')
    return render(request, "listar_cursos.html", {'lista':cursos})

def incluirCurso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('listarCurso')
            except:
                pass
    else:
        form = CursoForm()
    return render(request, "incluir_curso.html", {'form': form })

def editarCurso(request, id):
    curso = Curso.objects.get(codigo=id)
    form = CursoForm(instance=curso)

    if request.method == "POST":
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            try:
                form.save()
                return redirect('listarCurso')
            except:
                pass

    return render(request, "incluir_curso.html", {'form': form})

def excluirCurso(request, id):
    curso = Curso.objects.get(codigo=id)
    try:
        curso.delete()
    except:
        pass
    return redirect('listarCurso')
