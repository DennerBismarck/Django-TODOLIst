from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Tarefa
from api.serializers import TarefaSerializer

class Teste_API_Tarefa(APITestCase):

    def setUp(self): 
        self.tarefa1 = Tarefa.objects.create(
            titulo="Tarefa teste 1", 
            descricao="Fabrício lindo", 
            prazo="2024-05-20",
            situacao="NO"
        )
        self.tarefa2 = Tarefa.objects.create(
            titulo="Tarefa teste 2", 
            descricao="Márcio lindo - tarefa a ser deletada nos testes", 
            prazo="2024-05-21",
            situacao="AN"
        )
        self.tarefa3 = Tarefa.objects.create(
            titulo="Tarefa teste 3", 
            descricao="Taciano lindo", 
            prazo="2024-05-22",
            situacao="CO"
        )

    def test_get_all_tarefas(self):
        url = reverse('tarefa-list')
        response = self.client.get(url)
        tarefas = Tarefa.objects.all().order_by('id')
        serializer = TarefaSerializer(tarefas, many=True)

      
        expected_response = {
            'count': tarefas.count(),
            'next': None,
            'previous': None,
            'results': serializer.data
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_response)

    def test_search_tarefa(self):
        url = reverse('search-tarefa', kwargs={'id': self.tarefa1.id})
        response = self.client.get(url)
        serializer = TarefaSerializer(self.tarefa1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_add_tarefa(self):
        url = reverse('add-tarefa')
        data = {
            "titulo": "Nova Tarefa Teste",
            "descricao": "Nova Descrição",
            "prazo": "2024-07-20",
            "situacao": "NO"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tarefa.objects.count(), 4) 
        self.assertEqual(Tarefa.objects.get(id=4).titulo, "Nova Tarefa Teste")  

    def test_update_tarefa(self):
        url = reverse('update-tarefa', kwargs={'id': self.tarefa1.id})
        data = {
            "titulo": "Tarefa Atualizada" 
        }
        response = self.client.patch(url, data, format='json')
        self.tarefa1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.tarefa1.titulo, "Tarefa Atualizada")

    def test_delete_tarefa(self):
        url = reverse('delete-tarefa', kwargs={'id': self.tarefa2.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tarefa.objects.count(), 2)
