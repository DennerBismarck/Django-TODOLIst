#API Views
from rest_framework.response import Response #Python or Serialized data to JSON data
from rest_framework.decorators import api_view #Transforms function based views into APIView

@api_view(['GET'])
def ConfigTest(request):
    test = {'Título':'Desenvolver API', 'Descrição': 'Desenvolver API de To-Do List', 'Prazo':'09/05/2024', 'Data de Conclusão':'09/05/2024', 'Situação':'Em Andamento'}
    return Response(test)

