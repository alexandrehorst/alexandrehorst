<h1 align="center">:file_cabinet: PDF to Excel Converter README.md</h1>

## :memo: Descrição/ Description
Este programa foi criado para resolver um problema específico do meu trabalho tranformando uma lista de almoxarifado gerada em pdf em um arquivo excel passível de ser manipulado.
Antes essa transformação era realizada utilizando programas genéricos que realizam esse tipo de conversão. Entretanto, para termos a planilha perfeita ainda era necessário que o 
operador ajustasse manualmente as linhas e colunas que acabavam ficando mescladas no cerca de 1000 itens contidos no relatório de almoxarifado. Esse trabalho de ajuste manual 
durava aproximadamente 2 dias.

Para usar o programa, basta clicar no botão "selecionar arquivo" e uma janela será aberta para que o arquivo em pdf seja selecionado. Após selecionar o arquivo, basta clicar no 
botão "converter arquivo" e o arquivo excel será gerado dentro da pasta onde o programa estiver sendo executado.

Para desenvolver o programa, foi utilizado o módulo tabula que converte cada página documento em pdf num dataframe. Em seguida, são feitas manipulações nas colunas e linhas dos 
dataframes até que os mesmos fiquem no formato de colunas desejados. Com os dataframes corretamente configurados, os mesmos são mesclados num único dataframe que é salvo em excel.

Por questões de sigilo, não foram inseridos neste repositório os documentos em pdf nem as planilhas geradas. 

This program was created to solve a specific problem: to transform a PDF warehouse list into an Excel file that could be manipulated.
Before developing this program, this transformation was carried out using generic programs that perform this type of conversion. However, to have the perfect spreadsheet it was 
still necessary manual adjustments that would take about two days because many rows and columns were merged on these cases. Each list contains approximately 1000 items.

To use the program, you just simply click on the "select file" button and a window will open for the PDF file selection. After selecting the file, you have to click on the
"convert file" button and the excel file will be generated within the folder where the program is running.

To develop the program, the tabula module was used. This module converts each page of the PDF into a dataframe. Then, the dataframes` columns and rows are manipulated until they
get the desired format. With the dataframes correctly configured, they are merged into a single dataframe that is saved in Excel.

For reasons of confidentiality, neither PDF documents nor generated spreadsheets were included in this repository.

## ⚓: Dependências/ Dependencies
Este código foi desenvolvido utilizando o Jupyter Notebook versão 6.5.4 e o Python versão 3.11.4. Além disso, o código possui as seguintes dependências: módulo Selenium (selenium==4.13.0), Webdriver (ChromeDriver==116.0.5845.96), urllib.request (3.11) e beautifulsoup4 (bs4==4.12.2). O código depende também de um arquivo .py auxiliar contendo as credenciais do usuário para acesso ao site.

O arquivo do `webdriver.exe` deve ser colocado em um diretório que esteja no PATH do sistema operacional. Isso permitirá que o Python encontre o arquivo corretamente ao executar o código. Você pode colocar o `webdriver.exe` em um diretório como `C:\Windows` ou adicionar o diretório onde o arquivo está localizado ao PATH do sistema. Dessa forma, o Python conseguirá encontrá-lo durante a execução do código.

This code was developed using Jupyter Notebook version 6.5.4 and Python version 3.11.4. Additionally, the code has the following dependencies: Selenium module (selenium==4.13.0), Webdriver (ChromeDriver==116.0.5845.96), urllib.request (3.11) and beautifulsoup4 (bs4==4.12.2). The code also depends on an auxiliary credentials.py file containing the user's credentials to access the website.

The `webdriver.exe` file must be placed in a directory that is in the operating system's PATH. This will allow Python to find the file correctly when executing the code. You can place `webdriver.exe` in a directory like `C:\Windows` or add the directory where the file is located to the system PATH. This way, Python will be able to find it while executing the code.

## :books: Funcionalidades
* Realiza o download automático de todas as fotos que se encontram no site.
* Automatically downloads all photos found on the website.
 
## :wrench: Tecnologias utilizadas
* Webscraping

## :rocket: Rodando o projeto
Para rodar o código, o usuário precisa ter login e senha no site, os quais não serão disponibilizados aqui.

To run the code, the user must have credentias to acess the website.

## :dart: Status do projeto
O projeto está finalizado.

The project is done.
