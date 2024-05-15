# Django-TODOLIst
Django API made for the selection of Django Back-End Developer for LABENS.

# Documentação do Projeto
Este é um projeto Django que implementa uma API para gerenciamento de uma lista de tarefas (To-Do List). A API permite a criação, atualização, exclusão e busca de tarefas.

# Configuração do Ambiente de Desenvolvimento
**Pré-requisitos**
- Python 3.9 ou superior
- Docker
- Docker Compose

**Instalação**
1. Clone o repositório do projeto
2. Navegue até o diretório que contém o projeto (Onde o arquivo manage.py fica)
3. Construa e inicie os contêineres Docker com o seguinte comando: docker-compose up --build
4. Acesso a aplicação em: http://localhost:8000

# EndPoints
**Listar Todas as Tarefas**
- URL: /tarefas
- Método HTTP: GET
- Descrição: Retorna todas as tarefas cadastradas de forma paginada, 5 em 5 tarefas.
- Métodos:
  1. Search: Retorna tarefas que contém em seu título ou descrição a string passada: /tarefas/?search=string_de_busca.
  2. Page: Retorna a página de tarefas escolhida: /tarefas/?page=int_da_pagina
  3. Combinação das duas acima: /tarefas/search=exemplo&page=2
     
**Adicionar Nova Tarefa**
- URL: /tarefas/addTarefa
- Método HTTP: POST
- Descrição: Adiciona uma nova tarefa à lista.
  
**Buscar Tarefa por ID**
- URL: /tarefas/{id}
- Método HTTP: GET
- Parâmetros: id (ID da tarefa)
- Descrição: Retorna os detalhes de uma tarefa específica.
  
**Atualizar Tarefa**
- URL: /tarefas/{id}/editar
- Método HTTP: PUT
- Parâmetros: id (ID da tarefa)
- Descrição: Atualiza os detalhes de uma tarefa existente.
  
**Deletar Tarefa**
- URL: /tarefas/{id}/deletar
- Método HTTP: DELETE
- Parâmetros: id (ID da tarefa)
- Descrição: Remove uma tarefa da lista.

# Scripts Úteis
**Script de Testes unitários**
- Realiza testes de povoamento e em todos os endpoints
- python manage.py test

**Script de povoamento automático do banco de dados**
- Cria 15 tárefas diferentes no banco de dados
- python manage.py populate_tasks

