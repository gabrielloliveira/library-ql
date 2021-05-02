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
