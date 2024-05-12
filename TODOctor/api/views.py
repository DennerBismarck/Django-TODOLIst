#API Views
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from main.models import Tarefa
from .serializers import TarefaSerializer


@api_view(['GET'])
def ConfigTest(request):
    test = {'Título':'Desenvolver API', 'Descrição': 'Desenvolver API de To-Do List', 'Prazo':'09/05/2024', 'Data de Conclusão':'09/05/2024', 'Situação':'Em Andamento'}
    return Response(test)

@api_view(['GET'])
def TarefaGetAll(request):
    tarefas = Tarefa.objects.all()
    serializer = TarefaSerializer(tarefas, many = True)
    return Response(serializer.data)

