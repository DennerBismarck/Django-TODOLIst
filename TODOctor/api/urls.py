#API endpoints

from django.urls import path
from . import views

urlpatterns = [
    path('tarefas',views.TarefaGetAll, name='tarefa-list'),
    path('tarefas/addTarefa',views.AddTarefa, name='add-tarefa'),
    path('tarefas/<int:id>',views.TarefaGetOne, name='search-tarefa'),
    path('tarefas/<int:id>/editar', views.UpdateTarefa, name='update-tarefa'),
    path('tarefas/<int:id>/deletar',views.DeleteTarefa, name= 'delete-tarefa'),
]
