from django import forms
from django.forms import ModelForm

from cadastro.models import Curso, Turma


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class TurmaForm(ModelForm):
    class Meta:
        model = Turma
        fields = '__all__'

    dataInicio = forms.DateTimeField(
        label='Data de Início',
        widget=forms.DateTimeInput(
            format = '%Y-%m-%d %H:%M:%S',
            attrs={ 'type': 'datetime-local'}
        ),
        input_formats= ('%Y-%m-%d %H:%M:%S')
    )

    dataTermino = forms.DateTimeField(
        label='Data da Conclusão',
        widget=forms.DateTimeInput(
            format = '%Y-%m-%d %H:%M:%S',
            attrs={'type': 'datetime-local'}
        ),
        input_formats=('%Y-%m-%d %H:%M:%S')
    )
