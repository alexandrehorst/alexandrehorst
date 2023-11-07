<h1 align="center">:file_cabinet: Sistema de Gestão de Pacientes / Customer Management System README.md</h1>

## :memo: Descrição/ Description
Esse foi o primeiro projeto desenvolvido por mim utilizando Python. A motivação para escrevê-lo foi o fato de minha esposa ser dentista e eu querer ajudá-la a automatizar de alguma forma o seu consultório.

Este programa é baseado na manipulação de listas (cad -> a lista principal) que é composta por várias sub-listas, que contêm as informações de cada paciente. A lista pode ser carregada de uma planilha do Excel (atualmente) ou de um banco de dados (banco de dados SQL no futuro).
As sub-listas de dados do paciente são basicamente organizadas por: nome, telefone, endereço, número de identificação do paciente (chamado CPF no Brasil), profissão, e-mail, dia da próxima consulta, horário da próxima consulta e sinalização de envio de e-mail.

Recursos de software: registro de pacientes, agendamento/reagendamento/desmarcação de consultas (sincronizado com uma conta do Google Calendar), visualização de agendamento, visualização de dados do paciente, envio automático de e-mails N dias antes para pacientes que solicitam confirmação da consulta e integração com o Google Calendar (é necessário fazer algumas configurações na sua conta do Google e criar um token).

No final, é gerado um arquivo do Excel com todos os dados salvos. Sempre que você executar o programa, será perguntado se deseja importar os dados salvos anteriormente ou começar uma nova sessão. No futuro, pretendo ter uma integração com um banco de dados SQL (está no meu plano de ação).

Para o envio automático de e-mails, você precisará criar uma senha de aplicativo do Gmail e inserir uma conta do Gmail válida na linha 134.

Para incluir, ler, modificar ou excluir agendamentos usando a API do Google Calendar, é necessário seguir as ações descritas em https://developers.google.com/calendar/api/quickstart/python.

Tenha cuidado com o uso correto dos arquivos JSON.

Na configuração da sua conta do Google, você precisará criar um projeto e habilitar o uso da API.

É necessário instalar o módulo google-auth (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib).

No meu github há imagens da tela da aplicação (contendo dados de pacientes fictícios) contendo as operações de marcação de consulta (foto1.jpg), visualização das listagem de pacientes (foto2.jpg) e print da consulta agendada no google calendar (foto3.jpg). Há ainda uma terceira figura que ilustra o e-mail (e-mail_sistema_gerenciamento.jpg) que é enviado ao paciente quando a consulta se aproxima, ilustrando a integração do programa com a api do google e gmail. Cabe destacar ainda que o paciente marcado pode ser visualizado por ela no google calendar associado ao seu e-mail. 

#########################################################################################################################################################################################################

This was my first project developed using Python. The motivation for creating it was the fact that my wife is a dentist, and I wanted to help her automate her office in some way.

This program is based on list manipulation (cad -> the main list), which is composed of several sub-lists containing the information of each patient. The list can be loaded from an Excel spreadsheet (currently) or from a database (SQL database in the future). Patient data sub-lists are basically organized by: name, telephone, address, patient ID (called CPF in Brazil), profession, email, next appointment date, next appointment time, and email sending flag.

Software features: patient registration, appointment scheduling/rescheduling/cancellation (synchronized with a Google Calendar account), schedule viewing, patient data viewing, automatic email sending N days before an appointment for patients requesting confirmation, and integration with Google Calendar (requires some configuration in your Google account and token creation).

In the end, an Excel file is generated with all the saved data. Each time you run the program, you will be asked whether you want to import the previously saved data or start a new session. In the future, I plan to integrate it with an SQL database (it's in my action plan).

For automatic email sending, you will need to create a Gmail application password and enter a valid Gmail account on line 134.

To add, read, modify, or delete appointments using the Google Calendar API, you need to follow the actions described at https://developers.google.com/calendar/api/quickstart/python.

Be careful with the correct use of JSON files.

In your Google account settings, you will need to create a project and enable API usage.

You need to install the google-auth module (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib).

On my GitHub, there are screenshots of the application's interface (with fictitious patient data) showing the appointment scheduling operations (foto1.jpg), patient listing (foto2.jpg) and a printscreen of the scheduled appointment in Google Calendar (foto3.jpg). There's also a third image illustrating the email sent to the patient as the appointment approaches (e-mail_sistema_gerenciamento.jpg), demonstrating the program's integration with the Google API and Gmail. It's worth noting that the scheduled appointment can be viewed by her in the Google Calendar associated with her email.


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
* Cadastro de pacientes/ Patient registration;;
* Agendamento/reagendamento/desmarcação de consultas (sincronizado com uma conta do Google Calendar)/ Appointment scheduling/rescheduling/cancellation (synchronized with a Google Calendar account);
* Visualização de agendamento/ Schedule viewing;
* Visualização de dados do paciente/ Patient data viewing;
* Envio automático de e-mails de confirmação de consulta N dias antes/ Automatic email sending for appointment confirmation N days before;
* Integração com o Google Calendar (é necessário fazer algumas configurações na sua conta do Google e criar um token)/ Integration with Google Calendar (requires some configuration in your Google account and creating a token).

 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python
* Google API;
* Gmail integration;
* Pandas;
* Requests


## :rocket: Rodando o projeto/ Running the code
* Para o envio automático de e-mails, você precisará criar uma senha de aplicativo do Gmail e inserir uma conta do Gmail válida na linha 134.
* Para incluir, ler, modificar ou excluir agendamentos usando a API do Google Calendar, é necessário seguir as ações descritas em https://developers.google.com/calendar/api/quickstart/python.
* Tenha cuidado com o uso correto dos arquivos JSON.
* Na configuração da sua conta do Google, você precisará criar um projeto e habilitar o uso da API.
* É necessário instalar o módulo google-auth (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib).

Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.6.1
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.6.1)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando o comando: pip install pandas==1.1.5 google.auth===2.22.0 requests==2.27.1 google_auth_oauthlib==1.1.0 google-api-python-client==2.52.0 openpyxl==3.1.2
6) Executar o código: python "consultorio_v6.py"

To run the code, you need the following (using the Anaconda prompt):
* For automatic email sending, you'll need to create a Gmail application password and enter a valid Gmail account on line 134.
* To include, read, modify, or delete appointments using the Google Calendar API, you need to follow the actions described at https://developers.google.com/calendar/api/quickstart/python.
* Be cautious about the correct usage of JSON files.
* In your Google account settings, you will need to create a project and enable API usage.
* You need to install the google-auth module (pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib).

1. Create the virtual environment in a specific directory: conda create -n <venv_name> python=3.6.1
2. Activate the virtual environment: conda activate <venv_name>
3. Verify that everything is okay: python --version (you should see the message: Python 3.6.1)
4. Using the prompt, navigate to the directory where the code files are located.
5. Install the dependencies: pip install pandas==1.1.5 google.auth===2.22.0 requests==2.27.1 google_auth_oauthlib==1.1.0 google-api-python-client==2.52.0 openpyxl==3.1.2
6. Run the code: python "consultorio_v6.py"


## :dart: Status do projeto/ Project Status
Próximas atividades do projeto/ Project Roadmap:
* Create an executable version;
* Deploy it in Google Clouds;
* Integration with a SQL Database; and
* Create an user interface.
