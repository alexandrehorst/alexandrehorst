<h1 align="center">:file_cabinet: Carimbador Automático de Documentos/ Automatic Document Stamper README.md</h1>

## :memo: Descrição/ Description
Este programa permite que a partir de um conjunto de arquivos em formato PDF seja gerado um arquivo PDF final contendo todas as folhas carimbadas frente e verso e numeradas, caso o usuário deseje. 
O programa insere carimbo na parte frontal de cada página, numera as  páginas, se desejado, e insere carimbo "em branco" no verso de cada página restando apenas ao usuário imprimir o documento final em modo FRENTE E VERSO. Ao final serão gerados dois arquivos em pdf: 
"Arquivo_pronto.pdf" (conterá todas as páginas carimbadas e numeradas) e "Arquivo_sem_numeracao.pdf" (conterá apenas as páginas carimbadas). Para que as páginas sejam numeradas basta que o usuário preencha o campo "página inicial para numeração" contendo o número a ser 
inserido na primeira página. Caso, esse campo seja deixado em branco, as páginas não serão numeradas, mas apenas carimbadas. É importante destacar que ao final será gerado um arquivo em pdf (Arquivo_final.pdf) que deverá ser impresso colorido e no modo modo FRENTE E VERSO. 

=====================================================================================

This program allows, from a set of PDF files, the generation of a final PDF file containing all pages stamped on both sides and numbered, if the user desires. The program inserts a stamp on the front of each page, numbers the pages if desired, and inserts a "blank" stamp on the back of each page, leaving the user only to print the final document in double-sided mode. In the end, two PDF files will be generated: "Arquivo_pronto.pdf" (containing all stamped and numbered pages) and "Arquivo_sem_numeracao.pdf" (containing only the stamped pages).

To number the pages, the user needs to fill in the "initial page for numbering" field with the number to be inserted on the first page. If this field is left blank, the pages will not be numbered, only stamped. It is important to note that in the end, a PDF file (Arquivo_final.pdf) will be generated, which should be printed in color and in double-sided mode.




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

This code was developed using PyCharm 6.4.12 e o Python version 3.9.13. Additionally, the code has the following dependencies:
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
