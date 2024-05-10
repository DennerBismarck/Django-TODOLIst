from django.db import models

# Create your models here.

class Tarefa(models.Model):

    class situacoes_possiveis(models.TextChoices):
        NOVA = 'NO', 'Nova'
        EM_ANDAMENTO = 'AN', 'Em andamento'
        CONCLUIDA = 'CO', 'Concluida'
        CANCELADA = 'CA', 'Cancelada' 

    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=250, blank=True)
    prazo = models.DateField()
    data_conclusao = models.DateField(null=True, blank=True)
    situacao = models.CharField(choices=situacoes_possiveis, max_length=2)
    
