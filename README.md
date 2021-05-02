# LIBRARY-QL

Um projeto bem simples com propósito de estudos sobre uma api de uma livraria com Django e GraphQL

## Para executar o projeto

- Clone o projeto 👉🏽 ```git clone https://github.com/gabrielloliveira/library-ql.git```

Depois de clonar o projeto, você entra na pasta ```library-ql``` que acabou de ser criada. Você deve ter algum virtualenv criado. Na construção desse projeto, eu utilizei o Python na versão 3.8.2, mas funciona a partir da Python 3.6.

- Crie o virtualenv 👉🏽 ```python -m venv env```

- Ative o virtual env 👉🏽 ```source env/bin/active```

- Instale as dependências 👉🏽 ```pip install -r requirements.txt```

- Crie o arquivo .env com ajuda do script gerador de env files 👉🏽 ```python contrib/generate_env.py```

- Faça as migrations 👉🏽 ```python manage.py migrate```

- Rode o projeto 👉🏽 ```python manage.py runserver```

## Visualizando os dados

Para visualizar os dados, acesse [localhost:8000/graphql](http://localhost:8000/graphql) e rode as queries que você quiser. 

Como ainda é um projeto de estudos, eu não sei as melhores práticas. Utilizei django filters e relay.Node para fazer os filtros "mais dinâmicos".

Um exemplo de query para brincar (só vai mostrar algo se você tiver algum livro que tenha "tes" no nome):

```graphql
query{
  allBooks(name_Icontains: "tes") {
    edges {
      node {
        name
        uuid
      }
    }
  }
}
```
