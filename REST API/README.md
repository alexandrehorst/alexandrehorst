<h1 align="center">:file_cabinet: REST API Example README.md</h1>

## :memo: Descrição/ Description
Este é um projeto simples de API REST cujo objetivo é fornecer a receita de vendas de alguns produtos quando o usuário faz uma requisição (GET) a ela. A API foi desenvolvida usando o Flask.
A API importa as informações do banco de dados (o arquivo excel chamado "VENDAS - DEZ.xlsx"), processa-os usando o pandas e responde às requisições no formato JSON. Você pode fazer o upload da API para um servidor (Heroku ou Replit) com o arquivo excel e colocá-la online, ou pode executá-lo localmente usando uma IDE como o prompt do Anaconda, o PyCharm, o Spyder ou o Jupyter (rode o código REST_API.py). Há também um código para fazer as requisições à API (consulta_api.py).

No meu github há duas imagens: a primeira mostra a API online recebendo as conultas (requests) e a segunda mostra o resultado dessas consultas.

This is a simple REST API project whose objective is to provide the sales revenue of some products when the user makes a request (GET) to it. The API was developed using Flask.
The API import the informations from the database (the excel file named "VENDAS - DEZ.xlsx"), process it using pandas and respond the requests in the JSON format. You can upload the API to a server (Heroku or Replit) with the excel file and put it online or you can run it locally using the Anaconda Prompt or an IDE like PyCharm, Spyder or Jupyter. There is a code to make requests to the API Service (consulta_api.py).

On my GitHub, there are two images: the first one shows the online API receiving the requests (get), and the second one shows the results of those requests.

## ⚓ Dependências/ Dependencies
Este código foi desenvolvido utilizando o PyCharm 2022.3.2 e o Python versão 3.11.4. Além disso, o código possui as seguintes dependências:
* requests==2.31.0;
* openpyxl==3.1.2;
* pandas==2.1.1; e
* flask==3.0.0

This code was developed using PyCharm 2022.3.2 e o Python version 3.11.4. Additionally, the code has the following dependencies:
* requests==2.31.0;
* openpyxl==3.1.2;
* pandas==2.1.1; and
* flask==3.0.0

## :books: Funcionalidades/ Features
* Disponibiliza uma API REST para consulta usando o comando requests.
* Provides a REST API for querying using the 'requests' command.
 
## :wrench: Tecnologias utilizadas/ Technologies used
* Python;
* REST API;
* JSON;
* Requests; e
* Flask

## :rocket: Rodando o projeto/ Running the code
Na API em questão, utiliza-se como base de dados uma planilha de venda de diversos produtos (Vendas - Dez.xslx). Poderão ser feitas consultas para se obter o valor total do faturamento das vendas, o valor do faturamento obtido com a venda de cada produto e o valor do faturamento para um produto específico.

Para rodar o código, é importante que a planilha (Vendas - Dez.xslx) e os arquivos REST_API.py e consulta_api.py estejam no mesmo diretório.

Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.11.4
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.11.4)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando o comando: pip install requests==2.31.0 pandas==2.1.1 openpyxl==3.1.2 flask==3.0.0
6) Deixar o serviço da API online: python "REST_API.py"
7) Rodar o código para consulta a API: python "consulta_api.py"

* Para fazer uma consulta a API e verificar o faturamento total: requests.get('http://127.0.0.1:5000/') ou requests.get("http address")
Resposta: {"faturamento": value}, onde "faturamento" representa o faturamento total com vendas.

* Para fazer uma consulta a API e verificar o faturamento total de cada produto: requests.get('http://127.0.0.1:5000/vendas/produtos') ou requests.get("http address"/vendas/produtos)
  
Resposta: {"Valor Final":{"Bermuda":18450,"Bermuda Estampa":18590,"Bermuda Linho":25545,"Bermuda Liso":18683,"Bermuda Listrado":20212,"Bermuda Xadrez":20770,"Cal\u00e7a":23120,"Cal\u00e7a Estampa":21240,
"Cal\u00e7a Linho":27008,"Cal\u00e7a Liso":29830,"Cal\u00e7a Listrado":22806,"Cal\u00e7a Xadrez":15355,"Camisa":14600,"Camisa Estampa":19549,"Camisa Gola V":11100,"Camisa Gola V Estampa":17582,
"Camisa Gola V Linho":17110,"Camisa Gola V Liso":18644,"Camisa Gola V Listrado":11832,"Camisa Gola V Xadrez":13910,"Camisa Linho":21432,"Camisa Liso":16380,"Camisa Listrado":15120,"Camisa Xadrez":13440,
"Camiseta":27900,"Camiseta Estampa":26068,"Camiseta Linho":26091,"Camiseta Liso":26180,"Camiseta Listrado":23640,"Camiseta Xadrez":31800,"Casaco":32250,"Casaco Estampa":35328,"Casaco Linho":36478,
"Casaco Liso":34680,"Casaco Listrado":31473,"Casaco Xadrez":29267,"Chinelo":6240,"Chinelo Estampa":8732,"Chinelo Linho":10710,"Chinelo Liso":9940,"Chinelo Listrado":7592,"Chinelo Xadrez":8844,
"Cinto":22800,"Cinto Estampa":21527,"Cinto Linho":34472,"Cinto Liso":22781,"Cinto Listrado":26964,"Cinto Xadrez":23650,"Cueca":7350,"Cueca Estampa":8844,"Cueca Linho":10230,"Cueca Liso":8280,
"Cueca Listrado":8844,"Cueca Xadrez":8160,"Gorro":8720,"Gorro Estampa":11532,"Gorro Linho":12152,"Gorro Liso":12420,"Gorro Listrado":14744,"Gorro Xadrez":11730,"Meia":3360,"Meia Estampa":6250,
"Meia Linho":8112,"Meia Liso":5852,"Meia Listrado":3811,"Meia Xadrez":4469,"Mochila":39150,"Mochila Estampa":34625,"Mochila Linho":45717,"Mochila Liso":40020,"Mochila Listrado":22275,"Mochila Xadrez":41035,
"Polo":19760,"Polo Estampa":20562,"Polo Linho":28688,"Polo Liso":18495,"Polo Listrado":16688,"Polo Xadrez":19170,"Pulseira":6020,"Pulseira Estampa":11658,"Pulseira Linho":15162,"Pulseira Liso":9048,
"Pulseira Listrado":12403,"Pulseira Xadrez":10701,"Rel\u00f3gio":25200,"Rel\u00f3gio Estampa":25185,"Rel\u00f3gio Linho":29520,"Rel\u00f3gio Liso":24192,"Rel\u00f3gio Listrado":33354,"Rel\u00f3gio Xadrez":31458,
"Sapato":36400,"Sapato Estampa":44392,"Sapato Linho":59823,"Sapato Liso":54832,"Sapato Listrado":45738,"Sapato Xadrez":41952,"Short":8730,"Short Estampa":12864,"Short Linho":15827,"Short Liso":13608,
"Short Listrado":12036,"Short Xadrez":12100,"Sunga":12300,"Sunga Estampa":18720,"Sunga Linho":18327,"Sunga Liso":13110,"Sunga Listrado":13566,"Sunga Xadrez":17864,"Terno":82600,"Terno Estampa":101664,
"Terno Linho":102750,"Terno Liso":79920,"Terno Listrado":92879,"Terno Xadrez":70900,"T\u00eanis":25250,"T\u00eanis Estampa":32000,"T\u00eanis Linho":34986,"T\u00eanis Liso":34048,"T\u00eanis Listrado":25938,
"T\u00eanis Xadrez":29526}}

* Para fazer uma consulta a API e verificar o faturamento total específico de um produto: requests.get('http://127.0.0.1:5000/vendas/produtos/:nome_produto') ou requests.get("http address"/vendas/produtos/:nome_produto) 
Resposta: Response: {"Valor Final": 12300}

In this API example, a product sales spreadsheet (Vendas - Dez.xlsx) is used as the database. Queries can be made to obtain the total sales revenue, the revenue obtained from the sale of each product, and the revenue for a specific product.

To run the code, it is important that the spreadsheet (Sales - Dec.xlsx) and the files REST_API.py and consulta_api.py are in the same directory.

To run the code, you need to do the following (using the Anaconda prompt):

1) Create a virtual environment in a specific directory: conda create -n <venv_name> python=3.11.4
2) Activate the virtual environment: conda activate <venv_name>
3) Verify that everything is okay: python --version (you should see the message: Python 3.11.4)
4) Using the prompt, navigate to the directory where the code files are located.
5) Install the dependencies using the command: pip install requests==2.31.0 pandas==2.1.1 openpyxl==3.1.2 flask==3.0.0
6) Start the API service: python "REST_API.py"
7) Run the code to query the API: python "consulta_api.py"

* To make a query to the API and check the total revenue use: requests.get('http://127.0.0.1:5000/') or requests.get("http address")
Response: {"revenue": value}, where "revenue" represents the total sales revenue.

* To make a query to the API and check the total revenue for each product use: requests.get('http://127.0.0.1:5000/vendas/produtos') or requests.get("http address/vendas/produtos")
  
Response: {"Valor Final":{"Bermuda":18450,"Bermuda Estampa":18590,"Bermuda Linho":25545,"Bermuda Liso":18683,"Bermuda Listrado":20212,"Bermuda Xadrez":20770,"Cal\u00e7a":23120,"Cal\u00e7a Estampa":21240,
"Cal\u00e7a Linho":27008,"Cal\u00e7a Liso":29830,"Cal\u00e7a Listrado":22806,"Cal\u00e7a Xadrez":15355,"Camisa":14600,"Camisa Estampa":19549,"Camisa Gola V":11100,"Camisa Gola V Estampa":17582,
"Camisa Gola V Linho":17110,"Camisa Gola V Liso":18644,"Camisa Gola V Listrado":11832,"Camisa Gola V Xadrez":13910,"Camisa Linho":21432,"Camisa Liso":16380,"Camisa Listrado":15120,"Camisa Xadrez":13440,
"Camiseta":27900,"Camiseta Estampa":26068,"Camiseta Linho":26091,"Camiseta Liso":26180,"Camiseta Listrado":23640,"Camiseta Xadrez":31800,"Casaco":32250,"Casaco Estampa":35328,"Casaco Linho":36478,
"Casaco Liso":34680,"Casaco Listrado":31473,"Casaco Xadrez":29267,"Chinelo":6240,"Chinelo Estampa":8732,"Chinelo Linho":10710,"Chinelo Liso":9940,"Chinelo Listrado":7592,"Chinelo Xadrez":8844,
"Cinto":22800,"Cinto Estampa":21527,"Cinto Linho":34472,"Cinto Liso":22781,"Cinto Listrado":26964,"Cinto Xadrez":23650,"Cueca":7350,"Cueca Estampa":8844,"Cueca Linho":10230,"Cueca Liso":8280,
"Cueca Listrado":8844,"Cueca Xadrez":8160,"Gorro":8720,"Gorro Estampa":11532,"Gorro Linho":12152,"Gorro Liso":12420,"Gorro Listrado":14744,"Gorro Xadrez":11730,"Meia":3360,"Meia Estampa":6250,
"Meia Linho":8112,"Meia Liso":5852,"Meia Listrado":3811,"Meia Xadrez":4469,"Mochila":39150,"Mochila Estampa":34625,"Mochila Linho":45717,"Mochila Liso":40020,"Mochila Listrado":22275,"Mochila Xadrez":41035,
"Polo":19760,"Polo Estampa":20562,"Polo Linho":28688,"Polo Liso":18495,"Polo Listrado":16688,"Polo Xadrez":19170,"Pulseira":6020,"Pulseira Estampa":11658,"Pulseira Linho":15162,"Pulseira Liso":9048,
"Pulseira Listrado":12403,"Pulseira Xadrez":10701,"Rel\u00f3gio":25200,"Rel\u00f3gio Estampa":25185,"Rel\u00f3gio Linho":29520,"Rel\u00f3gio Liso":24192,"Rel\u00f3gio Listrado":33354,"Rel\u00f3gio Xadrez":31458,
"Sapato":36400,"Sapato Estampa":44392,"Sapato Linho":59823,"Sapato Liso":54832,"Sapato Listrado":45738,"Sapato Xadrez":41952,"Short":8730,"Short Estampa":12864,"Short Linho":15827,"Short Liso":13608,
"Short Listrado":12036,"Short Xadrez":12100,"Sunga":12300,"Sunga Estampa":18720,"Sunga Linho":18327,"Sunga Liso":13110,"Sunga Listrado":13566,"Sunga Xadrez":17864,"Terno":82600,"Terno Estampa":101664,
"Terno Linho":102750,"Terno Liso":79920,"Terno Listrado":92879,"Terno Xadrez":70900,"T\u00eanis":25250,"T\u00eanis Estampa":32000,"T\u00eanis Linho":34986,"T\u00eanis Liso":34048,"T\u00eanis Listrado":25938,
"T\u00eanis Xadrez":29526}}

* To make a query to the API and check the specific total revenue of a product use: requests.get('http://127.0.0.1:5000/vendas/produtos/:product_name') or requests.get("http address/vendas/produtos/:product_name") 
Response: Response: {"Valor Final": 12300}

## :dart: Status do projeto/ Project satus
O projeto está finalizado.

The project is done.
