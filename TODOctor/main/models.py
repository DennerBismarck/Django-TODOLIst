from django.db import models

# Create your models here.

class Tarefa(models.Model):

    situacoes_possiveis = [
        ('NO', 'Nova'),
        ('AN', 'Em Andamento'),
        ('CO', 'Concluída'),
        ('CA', 'Cancelada')
    ]
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=250, blank=True)
    prazo = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    situacao = models.CharField(choices=situacoes_possiveis, max_length=2)

    def __str__(self):
        return self.titulo
    
