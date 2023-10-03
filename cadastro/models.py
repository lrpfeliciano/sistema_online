from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)

    nome = models.CharField(max_length=200,
                            null=False)

    valor = models.DecimalField(max_digits=11,
                                decimal_places= 2,
                                null=False)
    def __str__(self):
        return self.nome

class Turma(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING)
    dataInicio = models.DateTimeField(null=False, verbose_name='Data de Início')
    dataTermino = models.DateTimeField(null=False, verbose_name='Data de Conclusão')

    def __str__(self):
        return f"{self.curso.nome} - {self.dataInicio} - {self.dataTermino}"
