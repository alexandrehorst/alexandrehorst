<h1 align="center">:file_cabinet: Sistema de Controle de Estoque/ Inventory Control System README.md</h1>

## :memo: Descrição/ Description
O Sistema de Cotação de Moedas converte vários moedas diferentes para Reais (R$) e possui 2 modos de operação:
1) Cotação específica para uma determinada moeda num determinado dia selecionados pelo usuário na GUI;
2) Múltiplas cotações inseridas por meio de uma planilha de excel contendo os códigos das moedas na primeira coluna (Ex: USD, EUR, BTC etc), observe a planilha Moedas.xlsx. Após selecionar o arquivo, o usuário informa o período que deseja a cotação inserindo a data no formato dd/mm/yy (são admitidos outros formatos também). Para obter a cotação, o usuário clica no botão "Atualizar cotação" e um arquivo em excel com as informações será gerado no mesmo diretório do arquivo de entrada.

A GUI foi desenvolvida utilizando o Tkinter e o programa realiza "requests" à API do awesome api para obter as cotações em reais (BRL). Além disso, utiliza-se o conceito de listas e o Pandas para manipular os dados e salvá-los em arquivos. Foi desenvolvido também uma lista suspensa com autocompletamento automático, assim, ao digitar algumas letras o programa já indica algumas opções de moedas a serem selecionadas.

Para saber o código das moedas utilizadas você precisa acessar o link: https://economia.awesomeapi.com.br/xml/available

No meu github há uma imagem da tela da aplicação e uma planilha contendo o resultado do pedido de cotação referente ao período mostrado na figura. 

This Currency Converter System is able to convert several different cuurecys to Reais (R$) from Brazil and has 2 operating modes:
1) In the first one, you can convert a specific currency in a specific date selected by the user in the GUI;

2) In secodnd way, you can convert multiple currencys at the same time for a specific period. You just have to enter the currency codes  through an excel spreadsheet containing the codes in the first column (Ex: USD, EUR, BTC), for example the file Moedas.xlsx. After the input file selection, the user informs the conversion period by inserting the date in the dd/mm/yy format (other formats are also accepted). Finally, the user must clicks on the button named "Atualizar cotação" and an excel file with the information will be generated in the same directory as the input file.

The GUI was developed using Tkinter and the program performs "requests" to an API called https://docs.awesomeapi.com.br/api-de-moedas to obtain the currencys convertiosn done in reais (BRL). In addition, the concept of lists and Pandas are used to manipulate data and save them in files. A Combobox with automatic autocompletion was also developed, so that when typing a few letters the program already indicates some currency options to be selected.

To get the currecys code you need to acess: https://economia.awesomeapi.com.br/xml/available

On my GitHub, there is an image of the application screen and a spreadsheet containing the quotation request result for the period shown in the figure.

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o PyCharm 2022.3.2 e o Python versão 3.11.4. Além disso, o código possui as seguintes dependências: 
* requests==2.31.0;
* openpyxl==3.1.2; e
* pandas==2.1.1. 

This code was developed using PyCharm 2022.3.2 e o Python version 3.11.4. Additionally, the code has the following dependencies:
* requests==2.31.0;
* openpyxl==3.1.2; and
* pandas==2.1.1.


## :books: Funcionalidades/ Features
* Busca a cotação de uma única moeda em relação ao Real (R$) para um dia específico ou retorna a cotação de diversas moedas (informadas por meio de uma planilha excel auxiliar) para um período específico.
* Searches for the price of a single currency in relation to the Real (R$) for a specific day or returns the price of several currencies (informed through an auxiliary Excel spreadsheet) for a specific period.
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python
* Pandas;
* REST API;
* Tkinter;
* Requests

## :rocket: Rodando o projeto/ Running the code
Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.11.4
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.11.4)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando o comando: pip install requests==2.31.0 pandas==2.1.1 openpyxl==3.1.2
6) Executar o código: python "Mini_projeto_v4.py"

To run the code, you need the following (using the Anaconda prompt):

1. Create the virtual environment in a specific directory: conda create -n <venv_name> python=3.11.4
2. Activate the virtual environment: conda activate <venv_name>
3. Verify that everything is okay: python --version (you should see the message: Python 3.11.4)
4. Using the prompt, navigate to the directory where the code files are located.
5. Install the dependencies: pip install requests==2.31.0 pandas==2.1.1 openpyxl==3.1.2
6. Run the code: python "Mini_projeto_v4.py"


## :dart: Status do projeto/ Project Status
O projeto está finalizado.

The project is done.

