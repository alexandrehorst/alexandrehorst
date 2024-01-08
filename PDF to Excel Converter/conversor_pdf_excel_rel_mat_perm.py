
# Código que converte o Relatório de Material Permanente do Siscofis em Excel
# Estratégia adotada: gera-se um Dataframe com as colunas conforme o df[u] nomeadas de Unnamed: 0 até Unnamed: N,
# junta-se o conteúdo de todas as colunas na primeira coluna, as demais são excluídas e inciam-se as manipulações
# na primeira coluna
# Ao importar as páginas da tabela são observadas as seguintes hipóteses
# H0: começa por Conta-contábil
# H1: começa por Conta-corrente
# H2: Começa por número (NR Ficha)
# H3: Começa por texto
# H4: Começa por número (V. Unit.)


import tabula
import pandas as pd
import numpy as np


# Função que verifica se uma "string" do tipo 0,00 é numérica tendo em vista que o módulo isnumeric() não o faz
def verifica_string(word):
    try:
        return type(float(word.replace('.', '').replace(',', '.'))) == float
    except:
        return False


def conversao_rel_mat_perm(nome_arquivo):
    # Método read_pdf do tabula para ler o arquivo PDF e converter em um DataFrame
    df = tabula.read_pdf(nome_arquivo, pages='all', area=(0, 0, 850, 590))

    for u in range(len(df)):

        # Cria o esqueleto do DF
        nomes_colunas = []

        # Renomeia as colunas de Unnamed: 0 até Unnamed: N
        for j in range(len(df[u].columns)):
            nomes_colunas.append('Unnamed:' + f' {j}')
        df[u].columns = nomes_colunas  # Nomeia as colunas

        # Concatenar o conteúdo das demais colunas na primeira
        df[u]['Unnamed: 0'] = df[u].apply(lambda row: ' '.join(map(str, row)), axis=1)
        df[u] = df[u].drop(nomes_colunas[1:], axis=1)  # Deleta as demais colunas

        for indice, linha in df[u].iterrows():  # Exclui nan das linhas
            linha['Unnamed: 0'] = str(linha['Unnamed: 0']).replace('nan', '')

        df[u] = df[u].reset_index(drop=True)  # reinicia os índices

        # Cria as colunas extras
        df[u]['NR Ficha'] = ''
        df[u]['Cod Mat'] = ''
        df[u]['Nome Padrão'] = ''
        df[u]['Conta Corrente'] = ''
        df[u]['Classificação'] = ''
        df[u]['Unid Med/ Cons'] = ''
        df[u]['V. Unit.'] = ''
        df[u]['Qtde'] = ''
        df[u]['Saldo'] = ''
        classificacao = ''
        conta = ''
        nome_padrao = ''
        num_ficha = ''
        cod_mat = ''
        unidade = ''
        flag = False
        i = 0

        # Iterar sobre as linhas do DataFrame
        for indice, linha in df[u].iterrows():
            # 'indice' é o índice da linha e 'linha' é uma série contendo os dados da linha
            if str(linha['Unnamed: 0']).startswith('Conta contábil'):  # H0
                classificacao = str(linha['Unnamed: 0']).split(':')[1]
            elif str(linha['Unnamed: 0']).startswith('Conta corrente'):  # H1
                conta = str(linha['Unnamed: 0']).split(':')[1]
            elif (str(linha['Unnamed: 0']).split()[0]).isnumeric():
                num_ficha = str(linha['Unnamed: 0']).split()[0]
                cod_mat = str(linha['Unnamed: 0']).split()[1]
                unidade = str(linha['Unnamed: 0']).split()[-1]
                if unidade != 'Unidade':
                    unidade = 'Não cadastrado'
                nome = str(linha['Unnamed: 0']).split()[2:-1]
                nome_padrao = " ".join([s for s in nome])
                i = indice
            elif indice > i and not (str(linha['Unnamed: 0']).split()[0]).isnumeric() and \
                    verifica_string(str(linha['Unnamed: 0']).split()[0]):
                linha['Saldo'] = str(linha['Unnamed: 0']).split()[2]
                linha['V. Unit.'] = str(linha['Unnamed: 0']).split()[0]
                linha['Qtde'] = str(linha['Unnamed: 0']).split()[1]
                linha['Classificação'] = classificacao
                linha['Conta Corrente'] = conta
                linha['Nome Padrão'] = nome_padrao
                linha['NR Ficha'] = num_ficha
                linha['Cod Mat'] = cod_mat
                linha['Unid Med/ Cons'] = unidade
                flag = True
            elif str(linha['Unnamed: 0']).startswith('QTDE TOTAL FICHA'):  # H5
                if flag:
                    linha['Cod Mat'] = f'QTDE TOTAL FICHA NR {num_ficha}:'  # Label: Qtde total ficha
                    linha['Nome Padrão'] = str(linha['Unnamed: 0']).split(':')[1].split()[0]  # Valor total ficha
                    linha['V. Unit.'] = f'QTDE TOTAL FICHA NR {num_ficha}:'
                    linha['Saldo'] = str(linha['Unnamed: 0']).split()[-1]  # Valor saldo total da ficha
                    flag = False
                else:
                    df[u].loc[indice-1, 'Classificação'] = classificacao
                    df[u].loc[indice-1, 'Conta Corrente'] = conta
                    df[u].loc[indice-1, 'Nome Padrão'] = nome_padrao
                    df[u].loc[indice-1, 'NR Ficha'] = num_ficha
                    df[u].loc[indice-1, 'Cod Mat'] = cod_mat
                    df[u].loc[indice-1, 'Unid Med/ Cons'] = unidade
                    linha['Cod Mat'] = f'QTDE TOTAL FICHA NR {num_ficha}:'  # Label: Qtde total ficha
                    linha['Nome Padrão'] = str(linha['Unnamed: 0']).split(':')[1].split()[0]  # Valor total ficha
                    linha['V. Unit.'] = f'QTDE TOTAL FICHA NR {num_ficha}:'
                    linha['Saldo'] = str(linha['Unnamed: 0']).split()[-1]  # Valor saldo total da ficha
            elif str(linha['Unnamed: 0']).startswith('SALDO TOTAL FICHAS CONTA'):
                # print(indice, 'H5')
                linha['V. Unit.'] = str(linha['Unnamed: 0']).split(':')[-2] + ':'  # label: Saldo total fichas conta
                linha['Saldo'] = str(linha['Unnamed: 0']).split(':')[-1]  # Valor saldo total fichas conta
            elif str(linha['Unnamed: 0']).startswith('SALDO TOTAL GERAL FICHAS'):
                # print(indice, 'H5')
                linha['V. Unit.'] = str(linha['Unnamed: 0']).split(':')[-2]  # label: Saldo total geral fichas
                linha['Saldo'] = str(linha['Unnamed: 0']).split(':')[-1]  # Valor saldo total geral fichas
            elif str(linha['Unnamed: 0']).split()[0].isalpha():  # H3
                # print(indice,'H3', nome_padrao)
                nome_padrao = nome_padrao + ' ' + str(linha['Unnamed: 0'])

        df[u] = df[u].drop('Unnamed: 0', axis=1)  # Exclui a coluna Unnamed: 0
        df[u].replace("", np.nan, inplace=True)  # Substituir células vazias por NaN para substituí-las
        df[u] = df[u].dropna(how='all')  # Exclui as linhas que possuam todas as células vazias
        df[u] = df[u].reset_index(drop=True)  # reinicia os índices

    # Concatena todas os DFs extraídos e formatados num DF único para posterior salvamento em Excel
    df_final = pd.concat(df, ignore_index=True)

    # Nome de salvamento do arquivo
    arquivo_final = nome_arquivo.replace('.pdf', '') + '.xlsx'

    # Salva o DataFrame como um arquivo Excel
    df_final.to_excel(arquivo_final, index=False)


if __name__ == '__main__':
    conversao_rel_mat_perm("RelContaContábil10201.pdf")
