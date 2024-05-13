#API Views
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from main.models import Tarefa
from .serializers import TarefaSerializer


@api_view(['GET'])
def ConfigTest(request):
    test = {'Título':'Desenvolver API', 'Descrição': 'Desenvolver API de To-Do List', 'Prazo':'09/05/2024', 'Data de Conclusão':'09/05/2024', 'Situação':'Em Andamento'}
    return Response(test)

@api_view(['GET'])
def TarefaGetAll(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5

    tarefas = Tarefa.objects.all()
    pagina_resultante = paginator.paginate_queryset(tarefas, request)

    serializer = TarefaSerializer(pagina_resultante, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def AddTarefa(request):
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)