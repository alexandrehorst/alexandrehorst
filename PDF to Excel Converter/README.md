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
This code was developed using PyCharm 2022.3.2 e o Python versão 3.9.13.

Além disso, o código possui as seguintes dependências: 
Additionally, the code has the following dependencies: 
absl-py==1.4.0
astunparse==1.6.3 
cachetools==5.3.1 
certifi==2023.7.22
charset-normalizer==3.2.0
distro==1.8.0
et-xmlfile==1.1.0
flatbuffers==23.5.26
gast==0.4.0
google-auth==2.22.0
google-auth-oauthlib==1.0.0
google-pasta==0.2.0
grpcio==1.57.0
h5py==3.9.0
idna==3.4
importlib-metadata==6.8.0
keras==2.13.1
libclang==16.0.6
llvmlite==0.40.1
Markdown==3.4.4
MarkupSafe==2.1.3
numba==0.57.1
numpy==1.24.2
oauthlib==3.2.2
openpyxl==3.1.2
opt-einsum==3.3.0
packaging==23.1
pandas==2.1.0
Pillow==10.0.0
protobuf==4.24.2
pyasn1==0.5.0
pyasn1-modules==0.3.0
python-dateutil==2.8.2
pytz==2023.3
requests==2.31.0
requests-oauthlib==1.3.1
rsa==4.9
six==1.16.0
tabula-py==2.6.0
tensorboard==2.13.0
tensorboard-data-server==0.7.1
tensorflow==2.13.0
tensorflow-estimator==2.13.0
tensorflow-intel==2.13.0
tensorflow-io-gcs-filesystem==0.31.0
termcolor==2.3.0
tkinter==8.6
typing_extensions==4.5.0
tzdata==2023.3
urllib3==1.26.16
Werkzeug==2.3.7
wrapt==1.15.0
zipp==3.16.2

## :books: Funcionalidades/ Functionalities
* Converte uma planilha com formato definido em PDF para uma planilha em excel. Além disso, realiza cálculos adicionais para controle de estoque.
* Converts a spreadsheet with a defined format in PDF to an Excel spreadsheet. In addition, it performs additional calculations for inventory control.
 
## :wrench: Tecnologias utilizadas
* Tkinter;
* Tabula module

## :rocket: Rodando o projeto
Esse código foi desenvolvido para uma planilha pré-definida, que por razões de sigilo não pode ser compartilhada aqui. Assim, não há garantias de que o código converterá 100% outros modelos de planilha no formato PDF.

This code was developed for a pre-defined spreadsheet, which for confidentiality reasons cannot be shared here. Therefore, there are no guarantees that the code will 100% convert other spreadsheet templates to PDF format.

## :dart: Status do projeto
O projeto está finalizado.

The project is done.