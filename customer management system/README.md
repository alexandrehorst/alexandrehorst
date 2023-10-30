<h1 align="center">:file_cabinet: Customer Management System README.md</h1>

## :memo: Descrição/ Description
Esse foi o primeiro projeto desenvolvido por mim utilizando Python. A motivação para escrevê-lo foi o fato de minha esposa ser dentista e eu queria ajudá-la a automatizar de alguma forma o seu consultório.

Este programa é baseado na manipulação de listas (cad -> a lista principal) que é composta por várias sub-listas, que contêm as informações de cada paciente. A lista pode ser carregada de uma planilha do Excel (atualmente) ou de um banco de dados (banco de dados SQL no futuro).
As sub-listas de dados do paciente são basicamente organizadas por: nome, telefone, endereço, número de identificação do paciente (chamado CPF no Brasil), profissão, e-mail, dia da próxima consulta, horário da próxima consulta e sinalização de envio de e-mail.

Recursos de software: registro de pacientes, agendamento/reagendamento/desmarcação de consultas (sincronizado com uma conta do Google Calendar), visualização de agendamento, visualização de dados do paciente, envio automático de e-mails N dias antes para pacientes que solicitam confirmação da consulta e integração com o Google Calendar (é necessário fazer algumas configurações na sua conta do Google e criar um token).

No final, é gerado um arquivo do Excel com todos os dados salvos. Sempre que você executar o programa, será perguntado se deseja importar os dados salvos anteriormente ou começar uma nova sessão. No futuro, pretendo ter uma integração com um banco de dados SQL (está no meu plano de ação).

Para o envio automático de e-mails, você precisará criar uma senha de aplicativo do Gmail e inserir uma conta do Gmail válida na linha 134.

Para incluir, ler, modificar ou excluir agendamentos usando a API do Google Calendar, é necessário seguir as ações descritas em https://developers.google.com/calendar/api/quickstart/python.

Tenha cuidado com o uso correto dos arquivos JSON.

Na configuração da sua conta do Google, você precisará criar um projeto e habilitar o uso da API.

É necessário instalar o módulo google-auth (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib).

No meu github há imagens da tela da aplicação (contendo dados de pacientes fictícios) conetndo as operações de marcação de consulta e visualização das listagem de pacientes. Há ainda um aterceira figura que ilustra o e-mail que é enviado ao paciente quando a consulta se aproxima, ilustrando a integração do programa com a api do google e gmail.
Cabe destacar ainda que o paciente marcado pode ser visualizado por ela no google calendar associado ao e-mail dela, 

This Currency Converter System is able to convert several different cuurecys to Reais (R$) from Brazil and has 2 operating modes:
1) In the first one, you can convert a specific currency in a specific date selected by the user in the GUI;

2) In secodnd way, you can convert multiple currencys at the same time for a specific period. You just have to enter the currency codes  through an excel spreadsheet containing the codes in the first column (Ex: USD, EUR, BTC), for example the file Moedas.xlsx. After the input file selection, the user informs the conversion period by inserting the date in the dd/mm/yy format (other formats are also accepted). Finally, the user must clicks on the button named "Atualizar cotação" and an excel file with the information will be generated in the same directory as the input file.

The GUI was developed using Tkinter and the program performs "requests" to an API called https://docs.awesomeapi.com.br/api-de-moedas to obtain the currencys convertiosn done in reais (BRL). In addition, the concept of lists and Pandas are used to manipulate data and save them in files. A Combobox with automatic autocompletion was also developed, so that when typing a few letters the program already indicates some currency options to be selected.

To get the currecys code you need to acess: https://economia.awesomeapi.com.br/xml/available

On my GitHub, there is an image of the application screen and a spreadsheet containing the quotation request result for the period shown in the figure.

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Spyder versão 5.2.2 e o Python versão 3.6.1. Além disso, o código possui as seguintes dependências:
* pandas==1.1.5;
* google.auth===2.22.0;
* requests==2.27.1;
* google_auth_oauthlib==1.1.0;
* google-api-python-client==2.52.0; e
* openpyxl==3.1.2.

This code was developed using Spyder version 5.2.2 and Python version 3.6.1. Additionally, the code has the following dependencies:
* pandas==1.1.5;
* google.auth===2.22.0;
* requests==2.27.1;
* google_auth_oauthlib==1.1.0;
* google-api-python-client==2.52.0; and
* openpyxl==3.1.2.


## :books: Funcionalidades/ Features
* Busca a cotação de uma única moeda em relação ao Real (R$) para um dia específico ou retorna a cotação de diversas moedas (informadas por meio de uma planilha excel auxiliar) para um período específico.
* Searches for the price of a single currency in relation to the Real (R$) for a specific day or returns the price of several currencies (informed through an auxiliary Excel spreadsheet) for a specific period.
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python
* Google API;
* Gmail integration;
* Pandas;
* Requests

## :rocket: Rodando o projeto/ Running the code
Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.6.1
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.6.1)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando o comando: pip install pandas==1.1.5 google.auth===2.22.0 requests==2.27.1 google_auth_oauthlib==1.1.0 google-api-python-client==2.52.0 openpyxl==3.1.2
6) Executar o código: python "consultorio_v6.py"

To run the code, you need the following (using the Anaconda prompt):

1. Create the virtual environment in a specific directory: conda create -n <venv_name> python=3.6.1
2. Activate the virtual environment: conda activate <venv_name>
3. Verify that everything is okay: python --version (you should see the message: Python 3.6.1)
4. Using the prompt, navigate to the directory where the code files are located.
5. Install the dependencies: pip install pandas==1.1.5 google.auth===2.22.0 requests==2.27.1 google_auth_oauthlib==1.1.0 google-api-python-client==2.52.0 openpyxl==3.1.2
6. Run the code: python "consultorio_v6.py"


## :dart: Status do projeto/ Project Status
O projeto está finalizado.

The project is done.