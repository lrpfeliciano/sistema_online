from django.urls import path

from cadastro import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste, name='teste'),
    path('print', views.print_em_html, name='print'),

    # Cursos
    path('listar_curso', views.listarCursos, name='listarCurso'),
    path('incluir_curso', views.incluirCurso, name='incluirCurso'),
    path('editar_curso/<int:id>', views.editarCurso, name='editarCurso'),
    path('excluir_curso/<int:id>', views.excluirCurso, name='excluirCurso'),

    # Turmas
    path('listar_turma', views.listarTurmas, name='listarTurmas'),
    path('incluirTurma', views.incluirTurma, name='incluirTurma'),
    path('editarTurma/<int:id>', views.editarTurma, name='editarTurma')

]