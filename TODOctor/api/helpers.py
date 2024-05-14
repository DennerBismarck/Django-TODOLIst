from main.models import Tarefa

#Auxiliar de procurar tarefas
def get_tarefa(id):
    try:
        return Tarefa.objects.get(pk=id)
    except Tarefa.DoesNotExist:
        return None