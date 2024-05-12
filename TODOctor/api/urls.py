#API endpoints

from django.urls import path
from . import views

urlpatterns = [
    path('tarefasList',views.TarefaGetAll, name='tarefa-list'),
]
