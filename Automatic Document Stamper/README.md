<h1 align="center">:file_cabinet: Carimbador Automático de Documentos/ Automatic Document Stamper README.md</h1>

## :memo: Descrição/ Description
Este programa nasceu da necessidade de se otimizar os processos adminitrativos de onde trabalho, substituindo um trabalho manual (necessidade de carimbar algumas dezenas ou centenas de folhas), por outro totalmente automatizado.  

O programa permite que a partir de um conjunto de arquivos em formato PDF seja gerado um arquivo PDF final contendo todas as folhas carimbadas frente e verso e numeradas, caso o usuário deseje. 

A aplicação insere um carimbo na parte frontal de cada página, numera as mesmas, se desejado, e insere um carimbo "em branco" no verso de cada página. Ao final, o programa gera  dois arquivos em pdf: "Arquivo_pronto.pdf" (conterá todas as páginas carimbadas e numeradas) e "Arquivo_sem_numeracao.pdf" (conterá apenas as páginas carimbadas). Para ter a documentação pronta, resta apenas ao usuário, imprimir o documento final colorido e no modo FRENTE E VERSO. 

Para que as páginas sejam numeradas basta que o usuário preencha o campo "página inicial para numeração" contendo o número a ser inserido na primeira página. Caso, esse campo seja deixado em branco, as páginas não serão numeradas, mas apenas carimbadas.

A interface de usuário (GUI) (window.png) foi desenvolvida utilizando-se o Proxlight Designer onde se cria um projeto, a partir do qual são gerados um conjunto de imagens (contidas no diretório GUI images) e um arquivo .py utilizando-se o Figma (interface de desenvolvimento baseada no módulo Tkinter). 

=====================================================================================

This program was born out of the need to optimize administrative processes at my workplace, replacing manual tasks (the need to stamp dozens or hundreds of pages) with a completely automated solution.

The program allows the generation of a final PDF file from a set of PDF files, containing all pages stamped on both sides and numbered, if desired by the user.

The application inserts a stamp on the front of each page, numbers the pages if desired, and inserts a "blank" stamp on the back of each page. In the end, the program generates two PDF files: "Arquivo_pronto.pdf" (containing all stamped and numbered pages) and "Arquivo_sem_numeracao.pdf" (containing only the stamped pages). To have the documentation ready, the user only needs to print the final document in color and in double-sided mode.

To number the pages, the user just needs to fill in the "initial page for numbering" field with the number to be inserted on the first page. If this field is left blank, the pages will not be numbered, only stamped.

The user interface (GUI) (window.png) was developed using Proxlight Designer, creating a project from which a set of images (contained in the GUI images directory) and a .py file are generated using Figma (a development interface based on the Tkinter module).

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Jupyter 6.4.12 e o Python versão 3.9.11. Além disso, o código possui as seguintes dependências: 
* Flask-Bcrypt==1.0.1; e
* pyodbc==4.0.34

This code was developed using PyCharm 6.4.12 e o Python version 3.9.11. Additionally, the code has the following dependencies:
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
