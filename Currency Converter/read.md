   O Sistema de Cotação de Moedas converte vários moedas diferentes para Reais (R$) e possui 2 modos de operação: 
1) Cotação específica para uma determinada moeda num determinado dia selecionados pelo usuário na GUI;
2) Múltiplas cotações inseridas por meio de uma planilha de excel contendo os códigos das moedas na primeira coluna (Ex: USD, EUR, BTC etc).

   Após selecionar o arquivo, o usuário informa o período que deseja a cotação inserindo a data no formato dd/mm/yy (são admitidos outros formatos também). Para obter a cotação, o usuário clica no botão "Atualizar cotação" e um arquivo em excel com as informações será gerado no mesmo diretório do arquivo de entrada.
   A GUI foi desenvolvida utilizando o Tkinter e o programa realiza "requests" à API do awesome api para obter as cotações em reais (BRL). Além disso, utiliza-se o conceito de listas e o Pandas para manipular os dados e salvá-los em arquivos. Foi desenvolvido também uma lista suspensa com autocompletamento automático, assim, ao digitar algumas letras o programa já indica algumas opções de moedas a serem selecionadas.
   Para saber o código das moedas utilizadas você precisa acessar o link: https://economia.awesomeapi.com.br/xml/available


   This Currency Converter System is able to convert several different cuurecys to Reais (R$) from Brazil and has 2 operating modes:
   1) In the first one, you can convert a specific currency in a specific date selected by the user in the GUI;
   2) In secodnd way, you can convert multiple currencys at the same time for a specific period.

      You just have to enter the currency codes through an excel spreadsheet containing the codes in the first column (Ex: USD, EUR, BTC). After the input file selection, the user informs the conversion period by inserting the date in the dd/mm/yy format (other formats are also accepted).
      Finally, the user must clicks on the button named "Atualizar cotação" and an excel file with the information will be generated in the same directory as the input file.
      The GUI was developed using Tkinter and the program performs "requests" to an API called https://docs.awesomeapi.com.br/api-de-moedas to obtain the currencys convertiosn done in reais (BRL). In addition, the concept of lists and Pandas are used to manipulate data and save them in files. A Combobox with automatic autocompletion was also developed, so that when typing a few letters the program already indicates some currency options to be selected.
      To get the currecys code you need to acess: https://economia.awesomeapi.com.br/xml/available
