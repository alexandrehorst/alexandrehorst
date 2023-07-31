# Miniprojeto de Tkinter (Sistema de Cotação de Moedas)
import tkinter as tk  # importa todo módulo Tkinter
import requests
from tkinter import ttk  # Extensão para criação de lista suspensa (combobox)
from tkinter import *
import re
from datetime import datetime, timedelta
from tkinter.filedialog import askopenfilename
import pandas as pd
import os


def periodo_cotacao(primeiro_dia, ultimo_dia):
    # Dia inicial e dia final no formato "yyyy/mm/dd"
    dia_inicial = datetime.strptime(primeiro_dia, "%Y/%m/%d")
    dia_final = datetime.strptime(ultimo_dia, "%Y/%m/%d")

    # Lista para armazenar os dias
    dias_periodo = []

    # Adiciona o dia inicial à lista
    dias_periodo.append(dia_inicial)

    # Incrementa um dia por vez e adiciona à lista até chegar ao dia final
    while dia_inicial < dia_final:
        dia_inicial += timedelta(days=1)
        dias_periodo.append(dia_inicial)
    # Formata os dias para o período usado
    for i, dia in enumerate(dias_periodo):
        dias_periodo[i] = dia.strftime("%d/%m/%y")
    return dias_periodo


# Fç que transforma a data de um formatdo de entrada para outro de saída
def formata_data(data, formato_entrada, formato_saida="%Y/%m/%d"):
    data_formatada = datetime.strptime(data, formato_entrada)
    data_formatada = data_formatada.strftime(formato_saida)
    return data_formatada


# Lista contendo os possíveis formatos de data
formato_data = ["YYYY-MM-DD", "DD-MM-YYYY", "DD/MM/YYYY", "YYYY/MM/DD", "DD/MM/YY", "DD-MM-YY"]


# Verifica se a data pertence a algum dos 4 padrões de data e, caso, positivo, retorna a data num formato padrão
# ("%Y/%m/%d")
def verificar_formato_data(data, formato):
    for u in formato:
        if u == "DD-MM-YYYY":
            padrao = r"\d{2}-\d{2}-\d{4}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%d-%m-%Y")
        elif u == "DD/MM/YYYY":
            padrao = r"\d{2}/\d{2}/\d{4}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%d/%m/%Y")
        elif u == "YYYY/MM/DD":
            padrao = r"\d{4}/\d{2}/\d{2}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%Y/%m/%d")
        elif u == "YYYY-MM-DD":
            padrao = r"\d{4}-\d{2}-\d{2}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%Y-%m-%d")
        elif u == "DD-MM-YY":
            padrao = r"\d{2}-\d{2}-\d{2}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%d-%m-%y")
        elif u == "DD/MM/YY":
            padrao = r"\d{2}/\d{2}/\d{2}"
            if re.fullmatch(padrao, data):
                return True, formata_data(data, "%d/%m/%y")
        else:
            return False, None


# Função que transforma timestamp em data
def transforma_timestamp(tmstp):
    data_real = datetime.fromtimestamp(int(tmstp))
    data_real = data_real.strftime('%d/%m/%y')
    return data_real


# Função para filtrar os itens da lista suspensa
def filter_combobox(*args):
    typed_text = moeda_var.get()
    filtered_items = []
    for v in moedas:
        if typed_text.lower() in v.lower():
            filtered_items.append(v)
    moeda['values'] = filtered_items


# Função que realiza o pedido de request
def realizar_request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,like Gecko) "
                             "Chrome/114.0.5735.199 Safari/537.36"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Verifica se houve algum erro na resposta
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("Erro HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Erro de conexão:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout de conexão:", errt)
    except requests.exceptions.RequestException as err:
        print("Erro durante a solicitação:", err)
    return None


# Função para buscar a cotação da API, onde cod_moeda é o cod da moeda, di é o dia inicial e df o dia final
def awesome_api(cod_moeda, di, df):
    print(cod_moeda)
    hj = datetime.now()  # Pega a data de hoje
    data_hj = hj.strftime("%Y/%m/%d")
    print(data_hj)
    if verificar_formato_data(di, formato_data)[0] and verificar_formato_data(df, formato_data)[0]:
        if type(cod_moeda) != list:  # COTAÇÃO ESPECÍFICA (não é lista)
            if verificar_formato_data(di, formato_data)[1] > data_hj or verificar_formato_data(df, formato_data)[1] > \
                    data_hj:  # Dia selecionado superior ao dia de hj
                mensagem_cotacao = tk.Label(text="Data selecionada superior a data de hoje!", fg='black', bg='#b0e0e6')
                mensagem_cotacao.grid(row=3, column=0, columnspan=2, sticky="NSEW")  # Adiciona o label à janela
            elif data_hj == verificar_formato_data(di, formato_data)[1]:  # Se a data selecionada for igual ao dia de hj
                url_hoje = 'https://economia.awesomeapi.com.br/last/' + cod_moeda
                cotacao = realizar_request(url_hoje)[cod_moeda + 'BRL']['bid']
            else:  # Se a data selecionada não for o dia de hj
                dia = verificar_formato_data(di, formato_data)[1].replace('/', '')
                url_diario = f"https://economia.awesomeapi.com.br/json/daily/" \
                             f"{cod_moeda}-BRL?start_date={dia}&end_date={dia}"
                cotacao = realizar_request(url_diario)[0]['bid']
            return cotacao
        else:  # MÚLTIPLAS COTAÇÕES (o número máximo de resultados é 360)
            dia1 = verificar_formato_data(di, formato_data)[1]
            dia2 = verificar_formato_data(df, formato_data)[1]
            # Se os dias solicitados forem maiores que o atual, a cotação será buscada até o dia atual
            if dia1 > data_hj:
                dia1 = data_hj
            if dia2 > data_hj:
                dia2 = data_hj
            periodo = periodo_cotacao(dia1, dia2)  # Cria uma lista do período da cotação
            mult_cotacoes = []
            for cod in cod_moeda:
                dia1 = dia1.replace('/', '')
                dia2 = dia2.replace('/', '')
                url_mult = f"https://economia.awesomeapi.com.br/json/daily/{cod}-BRL/" \
                           f"360?start_date={dia1}&end_date={dia2}"
                cotacoes = realizar_request(url_mult)
                cotacao_moeda = len(periodo)*['']
                for cotacao in cotacoes:
                    print('cotacao', cotacao)
                    data_transf = transforma_timestamp(cotacao['timestamp'])
                    for i, dia in enumerate(periodo):
                        if dia == data_transf:
                            cotacao_moeda[i] = cotacao['bid']
                print(cotacao_moeda)
                # Caso a API não retorne uma cotação, é feito um request específico para os dias faltantes
                for i, cotacao in enumerate(cotacao_moeda):
                    if cotacao == '':
                        dia = formata_data(periodo[i], "%d/%m/%y", "%Y/%m/%d").replace('/', '')
                        url_diario = f"https://economia.awesomeapi.com.br/json/daily/" \
                                     f"{cod}-BRL?start_date={dia}&end_date={dia}"
                        try:  # Caso a cotação não seja pega no request do período
                            cotacao_moeda[i] = realizar_request(url_diario)[0]['bid']
                        except IndexError:  # Caso o dia pleiteado seja final de semana
                            cotacao_moeda[i] = cotacao_moeda[i - 1]
                mult_cotacoes.append(cotacao_moeda)
                cotacao_moeda.insert(0, cod)
                cotacao_moeda = len(periodo) * ['']
            periodo.insert(0, 'Data')
            mult_cotacoes.insert(0, periodo)
            # print(mult_cotacoes)
            return mult_cotacoes


# Função que busca a cotação para a moeda e data selecionadas qdo a tecla "Pegar Cotação for acionada
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    data_preenchida = data_cotacao.get()
    if moeda_preenchida and data_preenchida:  # A rotina não continua se a moeda e data não foram selecionadas
        print('moeda preenchida', moeda_preenchida)
        for cod in cod_moedas:
            if cod_moedas[cod] == moeda_preenchida:
                cod_moeda = cod
        print(cod_moeda)
        mensagem_cotacao = tk.Label(text="Cotação não encontrada", fg='black', bg='#b0e0e6')  # Texto de msg não
        # encontrada
        mensagem_cotacao.grid(row=3, column=0, columnspan=2, sticky="NSEW")  # Adiciona o label à janela
        if cod_moeda:
            cotacao = awesome_api(cod_moeda, data_preenchida, data_preenchida)
            # Altera o label mensagem_cotaçao
            mensagem_cotacao["text"] = f'Cotação do {moeda_preenchida} é de {cotacao} reais'
    else:
        mensagem_cotacao = tk.Label(text="Moeda ou data não preenchidas", fg='black', bg='#b0e0e6')
        mensagem_cotacao.grid(row=3, column=0, columnspan=2, sticky="NSEW")  # Adiciona o label à janela


lst_moedas = []  # Será uma variável global para conectar a fç selecionar_arquivo() e atualizar_cotacao()
diretorio_entrada = ''


# Função que abre uma janela para selecionar o arquivo desejado
def selecionar_arquivo():
    global lst_moedas
    global diretorio_entrada
    caminho_arquivo = askopenfilename(title="Selecione um arquivo em Excel para abrir")
    diretorio_entrada = os.path.dirname(caminho_arquivo)
    mensagem_caminho_arquivo_entrada['text'] = caminho_arquivo  # Atualiza o caminho do arquivo
    df = pd.read_excel(caminho_arquivo)
    lst_moedas = list(df['Moedas'])
    return lst_moedas


# Função que atualiza as cotações para as moedas selecionadas
def atualizar_cotacao():
    global lst_moedas
    global diretorio_entrada
    print(lst_moedas)
    data_inicial_preenchida = data_inicial.get()
    data_final_preenchida = data_final.get()
    if data_inicial_preenchida and data_final_preenchida:  # A rotina não continua se moeda/ data não forem selecionadas
        mult_cotacoes = awesome_api(lst_moedas, data_inicial_preenchida, data_final_preenchida)
        df = pd.DataFrame(mult_cotacoes)  # Cria um DataFrame para incluir as infos de cotação
        # Salva o DataFrame num arquivo do Excel
        diretorio_saida = os.path.join(diretorio_entrada, f'mult_cotacoes{datetime.now().strftime("%d/%m/%y/%H/%M/%S").replace("/","")}.xlsx')
        df.to_excel(diretorio_saida, index=False)
        mensagem_arquivo_atualizado["text"] = "Arquivo de moedas atualizado com sucesso."


# inicia janela
janela = tk.Tk()

# Criar a variável de controle do combobox
moeda_var = StringVar()

# Cria uma lista suspensa (janela é onde irá aparecer a lista suspensa e values é a lista de valores)
moeda = ttk.Combobox(janela, textvariable=moeda_var)
moeda.grid(row=1, column=2, padx=10, pady=10, sticky="NSEW")

# Insere título da janela
janela.title("Sistema de Cotação de Moedas")

# Configura a cor do backgorund da janela
janela.configure(bg='#b0e0e6')

# Ajuste automático de linha(s) e coluna(s)
janela.rowconfigure([0, 12], weight=1)
janela.columnconfigure(2, weight=1)

# Cotação de 1 moeda específica
titulo1 = tk.Label(text="Cotação de 1 moeda específica", fg='black', bg='#b0e0e6', borderwidth=2, relief='solid')
titulo1.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="NSEW")

# Seleciona moeda
mensagem2 = tk.Label(text="Selecione a moeda que deseja consultar:", fg='black', bg='#b0e0e6')
mensagem2.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky="NSEW")

# Insere data
mensagem3 = tk.Label(text="Selecione o dia (DD/MM/AA) que deseja pegar a cotação:", fg='black', bg='#b0e0e6')
mensagem3.grid(row=2, column=0, padx=10, pady=10, columnspan=2, sticky="NSEW")

# Insere uma caixa de texto para que o usuário insira a data
data_cotacao = tk.Entry(fg='black', bg='white')
data_cotacao.grid(row=2, column=2, padx=10, pady=10, sticky="NSEW")

# Insere uma caixa de text para amsg de cotação
mensagem_cotacao = tk.Label(text="", fg='black', bg='#b0e0e6')
mensagem_cotacao.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")  # Adiciona o label à janela

# Cria um dicionário com os códigos do awesome API
cod_moedas = {'AED': 'Dirham dos Emirados', 'AFN': 'Afghani do Afeganistão', 'ALL': 'Lek Albanês',
              'AMD': 'Dram Armênio', 'ANG': 'Guilder das Antilhas', 'AOA': 'Kwanza Angolano', 'ARS': 'Peso Argentino',
              'AUD': 'Dólar Australiano', 'AZN': 'Manat Azeri', 'BAM': 'Marco Conversível', 'BBD': 'Dólar de Barbados',
              'BDT': 'Taka de Bangladesh', 'BGN': 'Lev Búlgaro', 'BHD': 'Dinar do Bahrein',
              'BIF': 'Franco Burundinense', 'BND': 'Dólar de Brunei', 'BOB': 'Boliviano', 'BSD': 'Dólar das Bahamas',
              'BTC': 'Bitcoin', 'BWP': 'Pula de Botswana', 'BYN': 'Rublo Bielorrusso', 'BZD': 'Dólar de Belize',
              'CAD': 'Dólar Canadense', 'CHF': 'Franco Suíço', 'CLP': 'Peso Chileno', 'CNH': 'Yuan chinês offshore',
              'CNY': 'Yuan Chinês', 'COP': 'Peso Colombiano', 'CRC': 'Colón Costarriquenho', 'CUP': 'Peso Cubano',
              'CVE': 'Escudo cabo-verdiano', 'CZK': 'Coroa Checa', 'DJF': 'Franco do Djubouti',
              'DKK': 'Coroa Dinamarquesa', 'DOGE': 'Dogecoin', 'DOP': 'Peso Dominicano', 'DZD': 'Dinar Argelino',
              'EGP': 'Libra Egípcia', 'ETB': 'Birr Etíope', 'ETH': 'Ethereum', 'EUR': 'Euro', 'FJD': 'Dólar de Fiji',
              'GBP': 'Libra Esterlina', 'GEL': 'Lari Georgiano', 'GHS': 'Cedi Ganês', 'GMD': 'Dalasi da Gâmbia',
              'GNF': 'Franco de Guiné', 'GTQ': 'Quetzal Guatemalteco', 'HKD': 'Dólar de Hong Kong',
              'HNL': 'Lempira Hondurenha', 'HRK': 'Kuna Croata', 'HTG': 'Gourde Haitiano', 'HUF': 'Florim Húngaro',
              'IDR': 'Rupia Indonésia', 'ILS': 'Novo Shekel Israelense', 'INR': 'Rúpia Indiana',
              'IQD': 'Dinar Iraquiano', 'IRR': 'Rial Iraniano', 'ISK': 'Coroa Islandesa', 'JMD': 'Dólar Jamaicano',
              'JOD': 'Dinar Jordaniano', 'JPY': 'Iene Japonês', 'KES': 'Shilling Queniano', 'KGS': 'Som Quirguistanês',
              'KHR': 'Riel Cambojano', 'KMF': 'Franco Comorense', 'KRW': 'Won Sul-Coreano', 'KWD': 'Dinar Kuwaitiano',
              'KYD': 'Dólar das Ilhas Cayman', 'KZT': 'Tengue Cazaquistanês', 'LAK': 'Kip Laosiano',
              'LBP': 'Libra Libanesa', 'LKR': 'Rúpia de Sri Lanka', 'LSL': 'Loti do Lesoto', 'LTC': 'Litecoin',
              'LYD': 'Dinar Líbio', 'MAD': 'Dirham Marroquino', 'MDL': 'Leu Moldavo', 'MGA': 'Ariary Madagascarense',
              'MKD': 'Denar Macedônio', 'MMK': 'Kyat de Mianmar', 'MNT': 'Mongolian Tugrik', 'MOP': 'Pataca de Macau',
              'MRO': 'Ouguiya Mauritana', 'MUR': 'Rúpia Mauriciana', 'MVR': 'Rufiyaa Maldiva',
              'MWK': 'Kwacha Malauiana', 'MXN': 'Peso Mexicano', 'MYR': 'Ringgit Malaio',
              'MZN': 'Metical de Moçambique', 'NAD': 'Dólar Namíbio', 'NGN': 'Naira Nigeriana',
              'NIO': 'Córdoba Nicaraguense', 'NOK': 'Coroa Norueguesa', 'NPR': 'Rúpia Nepalesa',
              'NZD': 'Dólar Neozelandês', 'OMR': 'Rial Omanense', 'PAB': 'Balboa Panamenho', 'PEN': 'Sol do Peru',
              'PGK': 'Kina Papua-Nova Guiné', 'PHP': 'Peso Filipino', 'PKR': 'Rúpia Paquistanesa',
              'PLN': 'Zlóti Polonês', 'PYG': 'Guarani Paraguaio', 'QAR': 'Rial Catarense', 'RON': 'Leu Romeno',
              'RSD': 'Dinar Sérvio', 'RUB': 'Rublo Russo', 'RWF': 'Franco Ruandês', 'SAR': 'Riyal Saudita',
              'SCR': 'Rúpias de Seicheles', 'SDG': 'Libra Sudanesa', 'SDR': 'DSE', 'SEK': 'Coroa Sueca',
              'SGD': 'Dólar de Cingapura', 'SOS': 'Shilling Somaliano', 'STD': 'Dobra São Tomé/Príncipe',
              'SVC': 'Colon de El Salvador', 'SYP': 'Libra Síria', 'SZL': 'Lilangeni Suazilandês',
              'THB': 'Baht Tailandês', 'TJS': 'Somoni do Tajiquistão', 'TND': 'Dinar Tunisiano',
              'TRY': 'Nova Lira Turca', 'TTD': 'Dólar de Trinidad', 'TWD': 'Dólar Taiuanês',
              'TZS': 'Shilling Tanzaniano', 'UAH': 'Hryvinia Ucraniana', 'UGX': 'Shilling Ugandês',
              'USD': 'Dólar Americano', 'USDT': 'Dólar Americano Turismo', 'UYU': 'Peso Uruguaio',
              'UZS': 'Som Uzbequistanês', 'VEF': 'Bolívar Venezuelano', 'VND': 'Dong Vietnamita',
              'VUV': 'Vatu de Vanuatu', 'XAF': 'Franco CFA Central', 'XAGG': 'Prata', 'XAU': 'Ouro',
              'XBR': 'Brent Spot', 'XCD': 'Dólar do Caribe Oriental', 'XOF': 'Franco CFA Ocidental',
              'XPF': 'Franco CFP', 'YER': 'Riyal Iemenita', 'ZAR': 'Rand Sul-Africano', 'ZMK': 'Kwacha Zambiana',
              'ZWL': 'Dólar Zimbabuense'}

# Cria uma lista com as chaves do dicionário
moedas = []
for item in cod_moedas:
    moedas.append(cod_moedas[item])

moeda['values'] = moedas

# Configurar a função de filtro para ser chamada sempre que o usuário digitar algo
moeda_var.trace('w', filter_combobox)

# Botão de busca da cotação
botao_buscar_cotacao = tk.Button(text="Pegar Cotação", fg='black', bg='#b0e0e6', command=buscar_cotacao)
botao_buscar_cotacao.grid(row=3, column=2, padx=10, pady=10,)  # Adiciona o botão na janela

# Cotação de Múltiplas Moedas
titulo2 = tk.Label(text="Cotação de Múltiplas Moedas", fg='black', bg='#b0e0e6', borderwidth=2, relief='solid')
titulo2.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="NSEW")

# Seleciona arquivo
mensagem_selecionar_arquivo = tk.Label(text="Selecione um arquivo em Excel com as moedas na coluna A:", fg='black',
                                       bg='#b0e0e6')
mensagem_selecionar_arquivo.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="NSEW")

# Botão para selecionar o arquivo
botao_selecionar_arquivo = tk.Button(text="Clique aqui para selecionar", fg='black', bg='#b0e0e6',
                                     command=selecionar_arquivo)
botao_selecionar_arquivo.grid(row=6, column=2, padx=10, pady=10)  # Adiciona o botão na janela

# Caminho do arquivo
mensagem_caminho_arquivo_entrada = tk.Label(text="Nenhum arquivo selecionado", fg='black', bg='#b0e0e6', anchor='e')
mensagem_caminho_arquivo_entrada.grid(row=7, column=0, columnspan=3, padx=10, pady=10, sticky="NSEW")

# Seleciona datas inicial e final
mensagem_data_inicial = tk.Label(text="Data Inicial (DD/MM/AA):", fg='black', bg='#b0e0e6')
mensagem_data_inicial.grid(row=8, column=0, sticky="NSEW")

data_inicial = tk.Entry(fg='black', bg='white')  # Caixa txt data inicial
data_inicial.grid(row=8, column=2)

mensagem_data_final = tk.Label(text="Data Final (DD/MM/AA):", fg='black', bg='#b0e0e6')
mensagem_data_final.grid(row=9, column=0, padx=10, pady=10, sticky="NSEW")

data_final = tk.Entry(fg='black', bg='white')  # Caixa txt data final
data_final.grid(row=9, column=2, padx=10, pady=10)

# Botão para atualizar cotações
botao_atualizar_cotacao = tk.Button(text="Atualizar Cotações", fg='black', bg='#b0e0e6', command=atualizar_cotacao)
botao_atualizar_cotacao.grid(row=11, column=0, padx=10, pady=10)  # Adiciona o botão na janela

# Msg de arquivo atualizado
mensagem_arquivo_atualizado = tk.Label(text="", fg='black', bg='#b0e0e6')
mensagem_arquivo_atualizado.grid(row=11, column=1, padx=10, pady=10, columnspan=2, sticky="NSEW")

# Botão para fechar programa
botao_fechar_programa = tk.Button(text="Fechar", fg='black', bg='#b0e0e6', command=janela.quit)
botao_fechar_programa.grid(row=12, column=2, padx=10, pady=10)  # Adiciona o botão na janela

# Roda o código continuamente permitindo que a janela fique continuamente na tela
janela.mainloop()
