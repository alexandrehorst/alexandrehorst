<h1 align="center">:file_cabinet: Sistema de Controle de Estoque/ Inventory Control System README.md</h1>

## :memo: Descrição/ Description
Este sistema foi desenvolvido em Python com o objetivo de realizar a inserção, a alteração, a exclusão e a leitura (CRUD) de informações referentes a itens ou a mercadorias de um banco de dados SQL (arquivo almoxarifado.db) fazendo o controle de estoque dos mesmos. 

A interface de usuário (GUI) (main_window.png) foi desenvolvida utilizando-se o Proxlight Designer onde se cria um projeto, a partir do qual são gerados um conjunto de imagens (contidas no diretório GUI images) e um arquivo .py utilizando-se o Figma (interface de desenvolvimento baseada no módulo Tkinter). 

O acesso ao sistema é protegido por senha (login_screen.png) de forma que apenas usuários cadastrados podem acessá-lo. O usuário padrão é "admin" e sua senha é "admin". Além disso, a senha dos usuários não fica acessível para todos que acessem o banco de dados, pois apenas o seu hash é salvo nele (na tabela users do banco de dados). Para cadastrar um novo usuário e senha no banco de dados, basta rodar o código password_creation.py.

O banco de dados (almoxarifado.db) é composto por 2 tabelas: estoque, que contem os dados dos itens cadastrados (nome, código de estoque, validade e quantidade), e users, que contem o nome e senha (hash) dos usuários. As figuras database_struture.png, users_table.png e inventory_table.png mostram mais detalhes do banco de dados e suas tabelas. Para uma melhor visualização dos mesmos foi utilizado o programa DB Browser for SQLite. 

O sistema permite as seguintes operações: 
1) Inclusão de itens no estoque mediante o fornecimento do nome, código, quantidade e validade do mesmo;
2) Exclusão de item do estoque informando o código de estoque do mesmo;
3) Registro dos itens utilizados (Uso de item) mediante o fornecimento do código de estoque e da quantidade utilizada; e
4) Procurar itens no estoque mediante o fornecimento do código de estoque (pesquisa específica), de uma palavra chave (mostra todos os itens que possuem aquela palavra) ou mostra todos os itens de estoque (se não for fornecida nenhuma informação).

Por fim, todas as operações realizadas no banco de dados são salvas num log (arquivo log_db.txt) onde são registradas todas as operações realizadas, o que foi alterado, quem alterou e quando alterou.

=====================================================================================

This system was developed in Python with the goal of performing the insertion, modification, deletion, and reading (CRUD) of information related to items or merchandise in an SQL database (almoxarifado.db file) to control their inventory.

The user interface (GUI) (main_window.png) was developed using Proxlight Designer, where a project is created, from which a set of images (located in the GUI images directory) and a .py file are generated using Figma (a development interface based on the Tkinter module).

Access to the system is password-protected (login_screen.png), allowing only registered users to access it. The default user is "admin," and the password is "admin." Additionally, the users' passwords are not accessible to everyone who accesses the database, as only their hash is stored in it (in the users table). To register a new user and password in the database, simply run the password_creation.py code.

The database (almoxarifado.db) consists of 2 tables: estoque, which contains data on registered items (name, stock code, expiration date and quantity), and users, which contains the name and users password (hash). The figures database_structure.png, users_table.png, and inventory_table.png show more details of the database and its tables. For a better view of them, the DB Browser for SQLite program was used.

The system allows the following operations:
1) Create new items in stock by providing their name, code, quantity, and expiration date;
2) Delete an item from stock by specifying its stock code;
3) Update an item quantity (Item Usage) by providing the stock code and the quantity used; and
4) Search for items (Read) in stock by providing the stock code (specific search), a keyword (displays all items containing that word), or displaying all stock items (if no information is provided).

Finally, all operations performed in the database are saved in a log (log_db.txt file) where all operations carried out, what was changed, who changed it, and when it was changed are recorded."


## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Jupyter 6.4.12 e o Python versão 3.9.13. Além disso, o código possui as seguintes dependências: 
* Flask-Bcrypt==1.0.1; e
* pyodbc==4.0.34

This code was developed using Jupyter 6.4.12 e o Python version 3.9.13. Additionally, the code has the following dependencies:
* Flask-Bcrypt==1.0.1; e
* pyodbc==4.0.34

## :books: Funcionalidades/ Features
* Inclusão de itens no estoque mediante o fornecimento do nome, código, quantidade e validade do mesmo;
* Exclusão de item do estoque informando o código de estoque do mesmo;
* Registro dos itens utilizados (Uso de item) mediante o fornecimento do código de estoque e da quantidade utilizada;
* Procurar itens no estoque mediante o fornecimento do código de estoque (pesquisa específica), de uma palavra chave (mostra todos os itens que possuem aquela palavra) ou mostra todos os itens de estoque (se não for fornecida nenhuma informação);
* Registro de todas as operações por meio de log; e
* Acesso apenas de usuários cadastrados.
  
===========================================================
* Create new items in stock by providing their name, code, quantity, and expiration date;
* Delete an item from stock by specifying its stock code;
* Update an item quantity (Item Usage) by providing the stock code and the quantity used; 
* Search for items (Read) in stock by providing the stock code (specific search), a keyword (displays all items containing that word), or displaying all stock items (if no information is provided);
* Recording of all operations through a log; and
* Access restricted to registered users.
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python
* SQL; and
* Tkinter.
  

## :rocket: Rodando o projeto/ Running the code
Antes de rodar o código é importante colocar todos os arquivos no mesmo diretório.

Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.9.13
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.9.13)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Instalar as dependências usando o comando: pip install Flask-Bcrypt==1.0.1 pyodbc==4.0.34
6) Executar o código: python "window_v2.py"


Before running the code, it's important to place all the files in the same directory.

To run the code, you need the following (using the Anaconda prompt):

1. Create the virtual environment in a specific directory: conda create -n <venv_name> python=3.9.13
2. Activate the virtual environment: conda activate <venv_name>
3. Verify that everything is okay: python --version (you should see the message: Python 3.9.13)
4. Using the prompt, navigate to the directory where the code files are located.
5. Install the dependencies: pip install Flask-Bcrypt==1.0.1 pyodbc==4.0.34
6. Run the code: python "window_v2.py"


## :dart: Status do projeto/ Project Status
O projeto está finalizado.

The project is done.

