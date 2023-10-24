<h1 align="center">:file_cabinet: REST API Example README.md</h1>

## :memo: Descrição/ Description
Este é um projeto simples de API REST cujo objetivo é fornecer a receita de vendas de alguns produtos quando o usuário faz uma solicitação (GET) a ela. A API foi desenvolvida usando o Flask.
A API importa dados do banco de dados (o arquivo excel chamado "VENDAS - DEZ.xlsx"), processa-os usando o pandas e responde às solicitações no formato JSON. Você pode fazer o upload da API para um servidor (Heroku ou Replit) com o arquivo excel e colocá-lo online, ou pode executá-lo localmente usando uma IDE como o PyCharm, o Spyder ou o Jupyter.

This is a simple REST API project whose objective is to provide the sales revenue of some products when the user makes a request (GET) to it. The API was developed using Flask.
The API import data from the database (the excel file named "VENDAS - DEZ.xlsx"), process it using pandas and respond the requests in the JSON format. You can upload the API to a server (Heroku or Replit) with the excel file and put it online or you can run it locally using an IDE like PyCharm, Spyder or Jupyter. 


## :books: Funcionalidades/ Functionalities
* Disponibiliza uma API REST para consulta usando o comando requests.
* Provides a REST API for querying using the 'requests' command.
 
## :wrench: Tecnologias utilizadas/ Tecnologies
* Python;
* REST API;
* JSON;
* Requests; e
* Flask

## :rocket: Rodando o projeto/ How to run the code
Na API em questão, utiliza-se como base de dados uma planilha de venda de diversos produtos (Vendas - Dez.xslx). Poderão ser feitas consultas para se obter o valor total do faturamento das vendas, o valor da venda de cada produto o valor faturado com a venda de cada produto.

Para rodar o código, é importante que a planilha (Vendas - Dez.xslx) esteja no mesmo diretório do arquivo REST API.py.

Para rodar a API, basta usar o comando (usando o prompt anaconda): python "REST API.py". Esse comando disponibilizará o serviço da API localmente no endereço (http://127.0.0.1:5000), a qual poderá receber consultas utilizando qualquer IDE (PyCharm, Jupyter, Sypder, etc). Para isso será preciso executar os seguintes comandos:
1) Consulta o valor do faturamento total
import requests
r=requests.get('http://127.0.0.1:5000/') ou requests.get("http address")
print(r.json())
Response: {"faturamento": value}, onde "faturamento" representa o faturamento total com vendas.

2) 
 

To run the code, the user must have credentias to acess the website.

-> To make the query you should use the following format: 
GET
1) "http address" (root directory)
Response: {"faturamento": value}, where "faturamento" means the total revenue 

Example: running the API in PyCharm
http://127.0.0.1:5000/
Response: {"faturamento": 2917311.0}

2) "http address"/vendas/produtos 
Response: {"product name": price}, returns the price of all products in the database one by one 

Example: running the API in PyCharm
http://127.0.0.1:5000/vendas/produtos

Response: {"faturamento": 2917311.0}
{"Valor Final":{"Bermuda":18450,"Bermuda Estampa":18590,"Bermuda Linho":25545,"Bermuda Liso":18683,"Bermuda Listrado":20212,"Bermuda Xadrez":20770,"Cal\u00e7a":23120,"Cal\u00e7a Estampa":21240,
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

3) "http address"/vendas/produtos/<product name>
Response: {"Valor Final": value}, where "Valor Final" means the final revenue for product selected 

Example: running the API in PyCharm
http://127.0.0.1:5000/vendas/produtos/Sunga
Response: {"Valor Final": 12300}

## :dart: Status do projeto/ Project satus
O projeto está finalizado.

The project is done.
