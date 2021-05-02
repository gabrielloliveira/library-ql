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

## Minhas primeiras impressões

Eu gosto bastante da proposta do graphql e acho que pode facilitar as coisas (dependendo do caso). Como minha stack principal é Django, resolvi fazer o teste e ver como se comporta em relação ao Django REST.

Algumas futuras melhorias que quero fazer é retirar o padrão que o JS tem para com as strings (esqueci o nome do padrão agora rsrs), que ele retira o underline e bota a próxima letra em uppercase.

Por exemplo:
O field created_at do meu modelo, fica como createdAt no graphql.

No momento, eu não gosto disso. Acho que, ao menos os campos da query, devem representar os campos reais do BD.

Com certeza deve ter uma explicação no âmbito de migrações de linguagens. Por exemplo, como o graphql vai ser executado com um framework JS, por isso que elez fazem esses "alias" com os campos e queries do modelo, para ajudar o prettier.

O fato é que hoje, no dia que escrevo isso, ainda não fui atrás para saber o motivo por trás. Hoje eu não gosto dessa conversão de nomes, mas nada é definitivo. Com o tempo, eu vou descobrir os melhores padrões pra me ajudar a desenvolver.

Outras melhorias para se lançar nesse projeto é fazer o CRUD completo. Por enquanto ele só faz a listagem e busca.

