BACKEND API

O arquivo main.py importa o app (variavel na qual instanciamos nosso objeto flask) e com isso 
usa o metodo run para rodar a aplicação. Ou seja, para rodar a aplicação, basta ativar a venv
e rodar "python main.py" no terminal, com isso vai inicializar um servidor e podemos utilizar 
ele para chamar os requests e rotas da API. A principio está num local host, mas precisamos 
descobrir como fica essa parte quando fizermos o deploy.

O diretorio flask_app é um pocote, pois tem o arquivo __init__.py. No init instanciamos e configuramos o objeto flask e o objeto do banco de dados.

No arquivo models serão definidos os modelos do banco de dados, da forma que estão la,
basta seguir o exemplo para os proximos. Depois para criar as colunas, é preciso utilizar 
o comando db.create_all(), é melhor fazer isso pelo terminal python.

No arquivo routes, estao definidas as rotas e as funções e metodos para interagir com 
o banco de dados.

PONTOS A VER 
- Segurança para o banco dedados, API, configurar alguma forma de autenticvação para que 
só o nosso app (doe vida) possa interagir com a api, se nao qualquer pessoa que fizer uma
requisição para o link da api pode mexer com o nosso banco de dados.

- Mudanças a serem feitas após o deploy

- Como fazer o deploy
