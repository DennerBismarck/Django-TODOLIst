# API Views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.db.models import Q
from main.models import Tarefa
from .serializers import TarefaSerializer
from .helpers import get_tarefa

@api_view(['GET'])
def TarefaGetAll(request):
    """
    Retorna uma lista paginada de tarefas.
    Se 'search' for fornecido, filtra as tarefas pelo título ou descrição.
    """
    
    search_query = request.query_params.get('search', None)

    tarefas = Tarefa.objects.all().order_by('id')

    if search_query:
        tarefas = Tarefa.objects.filter(
            Q(titulo__icontains=search_query) | Q(descricao__icontains=search_query)
        ).order_by('id')

    paginator = PageNumberPagination()
    paginator.page_size = 5

    pagina_resultante = paginator.paginate_queryset(tarefas, request)

    serializer = TarefaSerializer(pagina_resultante, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def AddTarefa(request):
    """
    Adiciona uma nova tarefa.
    """
    serializer = TarefaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def TarefaGetOne(request, id):
    """
    Retorna os detalhes de uma tarefa específica.
    """
    tarefa_procurada = get_tarefa(id)
    if tarefa_procurada is None:
        return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TarefaSerializer(tarefa_procurada)
    return Response(serializer.data)

@api_view(['PATCH'])
def UpdateTarefa(request, id):
    """
    Atualiza uma tarefa existente.
    """
    tarefa_procurada = get_tarefa(id)
    if tarefa_procurada is None:
        return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TarefaSerializer(tarefa_procurada, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def DeleteTarefa(request, id):
    """
    Deleta uma tarefa específica.
    """
    tarefa = get_tarefa(id)
    if tarefa is None:
        return Response({'error': 'Tarefa não encontrada'}, status=status.HTTP_404_NOT_FOUND)

    tarefa.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
