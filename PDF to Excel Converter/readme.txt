Este programa foi criado para resolver um problema específico do meu trabalho tranformando uma lista de almoxarifado gerada em pdf em um arquivo excel passível de ser manipulado.
Antes essa transformação era realizada utilizando programas genéricos que realizam esse tipo de conversão. Entretanto, para termos a planilha perfeita ainda era necessário que o 
operador ajustasse manualmente as linhas e colunas que acabavam ficando mescladas no cerca de 1000 itens contidos no relatório de almoxarifado. Esse trabalho de ajuste manual 
durava aproximadamente 2 dias.

Para usar o programa, basta clicar no botão "selecionar arquivo" e uma janela será aberta para que o arquivo em pdf seja selecionado. Após selecionar o arquivo, basta clicar no 
botão "converter arquivo" e o arquivo excel será gerado dentro da pasta onde o programa estiver sendo executado.

Para desenvolver o programa, foi utilizado o módulo tabula que converte cada página documento em pdf num dataframe. Em seguida, são feitas manipulações nas colunas e linhas dos 
dataframes até que os mesmos fiquem no formato de colunas desejados. Com os dataframes corretamente configurados, os mesmos são mesclados num único dataframe que é salvo em excel.

Por questões de sigilo, não foram inseridos neste repositório os documentos em pdf nem as planilhas geradas. 

#############################################################################################################################################
This program was created to solve a specific problem: to transform a PDF warehouse list into an Excel file that could be manipulated.
Before developing this program, this transformation was carried out using generic programs that perform this type of conversion. However, to have the perfect spreadsheet it was 
still necessary manual adjustments that would take about two days because many rows and columns were merged on these cases. Each list contains approximately 1000 items.

To use the program, you just simply click on the "select file" button and a window will open for the PDF file selection. After selecting the file, you have to click on the
"convert file" button and the excel file will be generated within the folder where the program is running.

To develop the program, the tabula module was used. This module converts each page of the PDF into a dataframe. Then, the dataframes` columns and rows are manipulated until they
get the desired format. With the dataframes correctly configured, they are merged into a single dataframe that is saved in Excel.

For reasons of confidentiality, neither PDF documents nor generated spreadsheets were included in this repository.
