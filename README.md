# Django REST API - Products Management

Este projeto é uma API REST_Framework desenvolvida usando Django e Django Rest Framework (DRF). A API permite a criação, leitura, atualização e exclusão (CRUD) de produtos.

## Funcionalidades

- **Listar produtos**: Obtenha uma lista de todos os produtos.
- **Detalhar um produto**: Obtenha os detalhes de um produto específico.
- **Criar um novo produto**: Adicione um novo produto ao banco de dados.
- **Atualizar um produto existente**: Modifique as informações de um produto.
- **Excluir um produto**: Remova um produto do banco de dados.


## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)


## Pré-requisitos

  - [Python 3.8+](https://www.python.org/downloads/)
  - [Pip](https://pip.pypa.io/en/stable/installation/)
  - [Virtualenv](https://virtualenv.pypa.io/en/latest/installation/)
    
 
## Instalação

Clone o repositório
    
    git clone https://github.com/seu-usuario/django-rest-api-produtos.git
    cd django-rest-api-produtos
    
 Crie e ative um ambiente virtual  

    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

 Instale as dependências do projeto

    pip install -r requirements.txt

Execute as migrações para criar o banco de dados

    python manage.py migrate

Inicie o servidor de desenvolvimento

    python manage.py runserver

Acesse a API em http://127.0.0.1:8000/ no seu navegador ou usando ferramentas como Postman ou cURL.

## Estrutura do Projeto

- models.py: Define o modelo 'Products', que representa um produto na base de dados.
- serializers.py: Contém o 'ProductsSerializer', que converte instâncias de 'Products' para JSON e vice-versa.
- views.py: Define a 'ProductsViewSet', que controla as operações CRUD.
- urls.py: Configura as rotas da API.
      

    
