<h1 align="center">:file_cabinet: Sistema de Controle de Estoque/ Inventory Control System README.md</h1>

## :memo: Descrição/ Description
Este sistema foi desenvolvido em Python com o objetivo de realizar a inserção, a alteração, a exclusão e a leitura (CRUD) de informações referentes a itens ou a mercadorias de um banco de dados SQL (arquivo almoxarifado.db) fazendo o controle de estoque dos mesmos. 

A interface de usuário (GUI) (fig1) foi desenvolvida utilizando-se o Proxlight Designer onde se cria um projeto, a partir do qual são gerados um conjunto de imagens (contidas no diretório GUI images) e um arquivo .py utilizando-se o Figma (interface de desenvolvimento baseada no módulo Tkinter). 

O acesso ao sistema é protegido por senha de forma que apenas usuários cadastrados podem acessá-lo. O usuário padrão é "admin" e sua senha é "admin". Além disso, a senha dos usuários não fica acessível para todos que acessem o banco de dados, pois apenas o seu hash é salvo nele (na tabela users do banco de dados). Para cadastrar um novo usuário e senha no banco de dados, basta rodar o código password_creation.py.

O banco de dados (almoxarifado.db) é composto por 2 tabelas: estoque, que contem os dados dos itens cadastrados (nome, código de estoque, validade e quantidade), e users, que contem o nome e senha (hash) dos usuários. As figuras database_struture.png, users_table.png e inventory_table.png mostram mais detalhes do banco de dados e suas tabelas. Para uma melhor visualização dos mesmos foi utilizado o programa DB Browser for SQLite. 

O sistema permite as seguintes operações: 
1) Inclusão de itens no estoque mediante o fornecimento do nome, código, quantidade e validade do mesmo;
2) Exclusão de item do estoque informando o código de estoque do mesmo;
3) Registro dos itens utilizados (Uso de item) mediante o fornecimento do código de estoque e da quantidade utilizada; e
4) Procurar itens no estoque mediante o fornecimento do código de estoque (pesquisa específica), de uma palavra chave (mostra todos os itens que possuem aquela palavra) ou mostra todos os itens de estoque (se não for fornecida nenhuma informação).

Por fim, toda as operações realizadas no banco de dados são salvas num log (arquivo log_db.txt) onde são registradas todas as operações realizadas, o que foi alterado, quem alterou e quando alterou.

English description


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
* Inclusão de itens no estoque mediante o fornecimento do nome, código, quantidade e validade do mesmo;
* Exclusão de item do estoque informando o código de estoque do mesmo;
* Registro dos itens utilizados (Uso de item) mediante o fornecimento do código de estoque e da quantidade utilizada;
* Procurar itens no estoque mediante o fornecimento do código de estoque (pesquisa específica), de uma palavra chave (mostra todos os itens que possuem aquela palavra) ou mostra todos os itens de estoque (se não for fornecida nenhuma informação);
* Registro de todas as operações por meio de log; e
* Acesso apenas de usuários cadastrados. 
 
## :wrench: Tecnologias utilizadas/ Technologies Used
* Python
* SQL;
* Tkinter;
* 

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

