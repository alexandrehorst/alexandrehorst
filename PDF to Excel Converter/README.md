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
Este código foi desenvolvido utilizando o PyCharm 2022.3.2 e o Python versão 3.9.13. 
Além disso, o código possui as seguintes dependências: openpyxl==3.1.2, Pillow==10.0.0 e tabula-py==2.6.0

This code was developed using PyCharm 2022.3.2 e o Python versão 3.9.13.
Additionally, the code has the following dependencies: openpyxl==3.1.2, Pillow==10.0.0 and tabula-py==2.6.0

## :books: Funcionalidades/ Functionalities
* Converte uma planilha com formato definido em PDF para uma planilha em excel. Além disso, realiza cálculos adicionais para controle de estoque.
* Converts a spreadsheet with a defined format in PDF to an Excel spreadsheet. In addition, it performs additional calculations for inventory control.
 
## :wrench: Tecnologias utilizadas
* Python;
* Tkinter;
* Tabula module

## :rocket: Rodando o projeto
Esse código foi desenvolvido para uma planilha pré-definida, que por razões de sigilo não pode ser compartilhada aqui. Assim, não há garantias de que o código converterá 100% outros modelos de planilha no formato PDF.

Para rodar o código é necessário o seguinte (usando o prompt do anaconda):
1) Criar o Ambiente virtual num determinado diretório: conda create -n <venv_name> python=3.9.13
2) Ativar o ambiente virtual: conda activate <venv_name>
3) Verificar se está tudo ok: python --version (deve ser mostrado a mensagem: Python 3.9.13)
4) Usando o prompt, buscar o diretório onde se encontram os arquivos do código.
5) Executar o código: python "main.py"

This code was developed for a pre-defined spreadsheet, which for confidentiality reasons cannot be shared here. Therefore, there are no guarantees that the code will 100% convert other spreadsheet templates to PDF format.

To run the code, you need the following (using the Anaconda prompt):

1. Create the virtual environment in a specific directory: `conda create -n <venv_name> python=3.9.13`
2. Activate the virtual environment: `conda activate <venv_name>`
3. Verify that everything is okay: `python --version` (you should see the message: Python 3.9.13)
4. Using the prompt, navigate to the directory where the code files are located.
5. Run the code: `python "main.py"`
   

## :dart: Status do projeto
O projeto está finalizado.

The project is done.
