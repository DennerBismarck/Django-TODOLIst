import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from main.models import Tarefa

class Command(BaseCommand):
    help = 'Popula o banco de dados com 15 tarefas, deixando data de conclusão de fora'

    def handle(self, *args, **options):
        situacoes = ['NO', 'EA', 'CO', 'CA']

        for  i in range (15):
            titulo = f"Tarefa {i+1}"
            descricao = f"Descrição da Tarefa {i+1}"
            prazo = datetime.now() + timedelta(days=random.randint(1, 30))
            situacao = random.choice(situacoes)

            #Sem data de conclusão
            Tarefa.objects.create(
                titulo=titulo,
                descricao=descricao,
                prazo=prazo,
                situacao=situacao
            )

        self.stdout.write(self.style.SUCCESS('15 tarefas criadas com sucesso'))

