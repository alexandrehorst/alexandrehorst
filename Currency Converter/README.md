<h1 align="center">:file_cabinet: Currency Converter README.md</h1>

## :memo: Descrição/ Description
O Sistema de Cotação de Moedas converte vários moedas diferentes para Reais (R$) e possui 2 modos de operação:
1) Cotação específica para uma determinada moeda num determinado dia selecionados pelo usuário na GUI;
2) Múltiplas cotações inseridas por meio de uma planilha de excel contendo os códigos das moedas na primeira coluna (Ex: USD, EUR, BTC etc). Após selecionar o arquivo, o usuário informa o período que deseja a cotação inserindo a data no formato dd/mm/yy (são admitidos outros formatos também). Para obter a cotação, o usuário clica no botão "Atualizar cotação" e um arquivo em excel com as informações será gerado no mesmo diretório do arquivo de entrada.

A GUI foi desenvolvida utilizando o Tkinter e o programa realiza "requests" à API do awesome api para obter as cotações em reais (BRL). Além disso, utiliza-se o conceito de listas e o Pandas para manipular os dados e salvá-los em arquivos. Foi desenvolvido também uma lista suspensa com autocompletamento automático, assim, ao digitar algumas letras o programa já indica algumas opções de moedas a serem selecionadas.

Para saber o código das moedas utilizadas você precisa acessar o link: https://economia.awesomeapi.com.br/xml/available

This Currency Converter System is able to convert several different cuurecys to Reais (R$) from Brazil and has 2 operating modes:
1) In the first one, you can convert a specific currency in a specific date selected by the user in the GUI;

2) In secodnd way, you can convert multiple currencys at the same time for a specific period. You just have to enter the currency codes  through an excel spreadsheet containing the codes in the first column (Ex: USD, EUR, BTC). After the input file selection, the user informs the conversion period by inserting the date in the dd/mm/yy format (other formats are also accepted). Finally, the user must clicks on the button named "Atualizar cotação" and an excel file with the information will be generated in the same directory as the input file.

The GUI was developed using Tkinter and the program performs "requests" to an API called https://docs.awesomeapi.com.br/api-de-moedas to obtain the currencys convertiosn done in reais (BRL). In addition, the concept of lists and Pandas are used to manipulate data and save them in files. A Combobox with automatic autocompletion was also developed, so that when typing a few letters the program already indicates some currency options to be selected.

To get the currecys code you need to acess: https://economia.awesomeapi.com.br/xml/available

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Jupyter Notebook versão 6.5.4 e o Python versão 3.11.4. Além disso, o código possui as seguintes dependências: módulo Selenium (selenium==4.13.0), Webdriver (ChromeDriver==116.0.5845.96), urllib.request (3.11) e beautifulsoup4 (bs4==4.12.2). O código depende também de um arquivo .py auxiliar contendo as credenciais do usuário para acesso ao site.

O arquivo do `webdriver.exe` deve ser colocado em um diretório que esteja no PATH do sistema operacional. Isso permitirá que o Python encontre o arquivo corretamente ao executar o código. Você pode colocar o `webdriver.exe` em um diretório como `C:\Windows` ou adicionar o diretório onde o arquivo está localizado ao PATH do sistema. Dessa forma, o Python conseguirá encontrá-lo durante a execução do código.

This code was developed using Jupyter Notebook version 6.5.4 and Python version 3.11.4. Additionally, the code has the following dependencies: Selenium module (selenium==4.13.0), Webdriver (ChromeDriver==116.0.5845.96), urllib.request (3.11) and beautifulsoup4 (bs4==4.12.2). The code also depends on an auxiliary credentials.py file containing the user's credentials to access the website.

The `webdriver.exe` file must be placed in a directory that is in the operating system's PATH. This will allow Python to find the file correctly when executing the code. You can place `webdriver.exe` in a directory like `C:\Windows` or add the directory where the file is located to the system PATH. This way, Python will be able to find it while executing the code.

## :books: Funcionalidades
* Realiza o download automático de todas as fotos que se encontram no site.
* Automatically downloads all photos found on the website.
 
## :wrench: Tecnologias utilizadas
* Pandas;
* REST API;
* Tkinter;
* Requests

## :rocket: Rodando o projeto
Para rodar o código, o usuário precisa ter login e senha no site, os quais não serão disponibilizados aqui.

To run the code, the user must have credentias to acess the website.

## :dart: Status do projeto
O projeto está finalizado.

The project is done.
