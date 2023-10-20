<h1 align="center">:file_cabinet: Currency Converter README.md</h1>

## :memo: Descrição/ Description
O Sistema de Cotação de Moedas converte vários moedas diferentes para Reais (R$) e possui 2 modos de operação:
1) Cotação específica para uma determinada moeda num determinado dia selecionados pelo usuário na GUI;
2) Múltiplas cotações inseridas por meio de uma planilha de excel contendo os códigos das moedas na primeira coluna (Ex: USD, EUR, BTC etc), observe a planilha Moedas.xlsx. Após selecionar o arquivo, o usuário informa o período que deseja a cotação inserindo a data no formato dd/mm/yy (são admitidos outros formatos também). Para obter a cotação, o usuário clica no botão "Atualizar cotação" e um arquivo em excel com as informações será gerado no mesmo diretório do arquivo de entrada.

A GUI foi desenvolvida utilizando o Tkinter e o programa realiza "requests" à API do awesome api para obter as cotações em reais (BRL). Além disso, utiliza-se o conceito de listas e o Pandas para manipular os dados e salvá-los em arquivos. Foi desenvolvido também uma lista suspensa com autocompletamento automático, assim, ao digitar algumas letras o programa já indica algumas opções de moedas a serem selecionadas.

Para saber o código das moedas utilizadas você precisa acessar o link: https://economia.awesomeapi.com.br/xml/available

This Currency Converter System is able to convert several different cuurecys to Reais (R$) from Brazil and has 2 operating modes:
1) In the first one, you can convert a specific currency in a specific date selected by the user in the GUI;

2) In secodnd way, you can convert multiple currencys at the same time for a specific period. You just have to enter the currency codes  through an excel spreadsheet containing the codes in the first column (Ex: USD, EUR, BTC), for example the file Moedas.xlsx. After the input file selection, the user informs the conversion period by inserting the date in the dd/mm/yy format (other formats are also accepted). Finally, the user must clicks on the button named "Atualizar cotação" and an excel file with the information will be generated in the same directory as the input file.

The GUI was developed using Tkinter and the program performs "requests" to an API called https://docs.awesomeapi.com.br/api-de-moedas to obtain the currencys convertiosn done in reais (BRL). In addition, the concept of lists and Pandas are used to manipulate data and save them in files. A Combobox with automatic autocompletion was also developed, so that when typing a few letters the program already indicates some currency options to be selected.

To get the currecys code you need to acess: https://economia.awesomeapi.com.br/xml/available

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o PyCharm 2022.3.2 e o Python versão 3.9.13.

This code was developed using PyCharm 2022.3.2 e o Python versão 3.9.13.

Além disso, o código possui as seguintes dependências:

Additionally, the code has the following dependencies:

![dependencies](https://github.com/alexandrehorst/alexandrehorst/assets/98498152/d6396e74-abdb-4f1a-bd55-4e77d445163d)


## :books: Funcionalidades
* Busca a cotação de uma única moeda em relação ao Real (R$) para um dia específico ou retorna a cotação de diversas moedas (informadas por meio de uma planilha excel auxiliar) para um período específico.
* Searches for the price of a single currency in relation to the Real (R$) for a specific day or returns the price of several currencies (informed through an auxiliary Excel spreadsheet) for a specific period.
 
## :wrench: Tecnologias utilizadas
* Pandas;
* REST API;
* Tkinter;
* Requests

## :rocket: Rodando o projeto
Para rodar o código, o usuário precisa instala os seguintes módulos: requests, pandas, openpyxl, opencv e numpy, utilizando o comando: "pip install <module_name>".

Para rodar o código utilize o comando: "python Mini_projeto_v4.py"

To run the code, the user needs to install the following modules: requests, pandas, openpyxl, opencv and numpy, using the command: "pip install <module_name>".

To run the code use the command: "python Mini_projeto_v4.py"

## :dart: Status do projeto
O projeto está finalizado.

The project is done.
