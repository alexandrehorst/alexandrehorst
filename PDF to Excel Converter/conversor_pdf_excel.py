import tabula
import pandas as pd
import numpy as np
# import openpyxl
# from openpyxl.styles import Alignment


# # Função para salvamento personalizado do arquivo
# def configura_arquivo(nome_arquivo):
#     # ajusta o alinhamento do texto
#     # alinhamento_colunas = {'NR ORD': 'center', 'Especificação': 'left', 'Nr Ficha': 'center', 'Conta Corrente': 'center',
#     #              ' Classificação': 'center', 'Unid Med/ Cons': 'center', 'Qtde': 'center', 'Valor Unitário': 'center',
#     #              'Valor Total': 'center', 'Situação': 'center'}
#     # Definir a largura das colunas
#     largura_colunas = {'NR ORD': 20, 'Especificação': 50, 'Nr Ficha': 20, 'Conta Corrente': 20, 'Classificação': 20,
#                        'Unid Med/ Cons': 20, 'Qtde': 20, 'Valor Unitário': 30, 'Valor Total': 30, 'Situação': 20,
#                        '% individual': 20, '% acumulada': 20, 'Classificação ABC': 20}
#
#     # Abre um arquivo Excel
#     workbook = openpyxl.load_workbook(nome_arquivo)
#
#     # Seleciona a Sheet ativa
#     sheet = workbook.active
#     # Se quiser pegar pelo nome faça -> sheet = workbook['nome_da_sheet']
#
#     # Definir a largura das colunas
#     largura_colunas = {'A': 15, 'B': 100, 'C': 20}
#     for column, width in largura_colunas.items():
#         sheet.column_dimensions[column].width = width
#
#     # Ajustar o alinhamento do texto
#     for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
#         for cell in row:
#             cell.alignment = Alignment(horizontal='center', vertical='center')
#
#     workbook.save(f'teste_output.xlsx')
#     workbook.close()


# Função que enquadra na classificação ABC
def classifica(percentual_acumulado):
    if percentual_acumulado < 80:
        return 'A'
    elif 80 < percentual_acumulado < 95:
        return 'B'
    else:
        return 'C'


# Função que junta as colunas de um DF
def concatenar_colunas(row):
    return ' '.join(str(value) for value in row)


# Função para excluir o nan das linhas do DF
def excluir_nan(row):
    row_sem_nan = list(filter(lambda x: x != 'nan', row.split()))
    row_sem_nan = ' '.join(row_sem_nan)
    return row_sem_nan


# Função que converte o arquivo de pdf para excel
def conversao(caminho_arquivo_pdf):
    # Método read_pdf do tabula para ler o arquivo PDF e converter em um DataFrame
    df = tabula.read_pdf(caminho_arquivo_pdf, pages='all')

    for u in range(len(df)):
        if u == 0:
            df[u].columns = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2']
            df[u] = df[u].iloc[8:]  # Considera o dataframe apenas a partir da linha 8
            # Obter info do usuário que gerou o relatório do SISCOMIS
            indice_info_usuario = int(str(df[u]['Unnamed: 0'].tail(1)).split()[0])
            info_usuario = df[u]['Unnamed: 1'].iloc[indice_info_usuario - 8]
        else:
            df[u].columns = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4']
            df[u] = df[u].iloc[1:]  # Considera o dataframe apenas a partir da linha 2
        # Elimina as linhas que contenham as palavras 'SUB TOTAL', 'Conta contábil' e "Inventário emitido pelo SISCOFIS"
        df[u] = df[u][~df[u].apply(lambda row: row.astype(str).str.contains("SUB TOTAL").any(), axis=1)]
        df[u] = df[u][~df[u].apply(lambda row: row.astype(str).str.contains("Inventário emitido pelo SISCOFIS").any(),
                                   axis=1)]
        df[u] = df[u].reset_index(drop=True)  # reinicia os índices

        # Cria as colunas extras
        df[u]['NR ORD'] = ''
        df[u]['Especificação'] = ''
        df[u]['Nr Ficha'] = ''
        df[u]['Conta Corrente'] = ''
        df[u]['Classificação'] = ''
        df[u]['Unid Med/ Cons'] = ''
        df[u]['Qtde'] = ''
        df[u]['Valor Unitário'] = ''
        df[u]['Valor Total'] = ''
        df[u]['Situação'] = ''
        conta_corrente = ''
        classificacao = ''
        nr_ref = 1

        if u == 0:
            for i in range(len(df[u])):
                if str(df[u]['Unnamed: 0'].iloc[i]).startswith('Conta'):  # Caso a linha inicie por Conta contábil
                    k = 0
                    df[u].loc[i, 'Unnamed: 0'] = str(df[u]['Unnamed: 0'].iloc[i]) + " " + str(
                        df[u]['Unnamed: 1'].iloc[i])
                    conta_corrente = str(df[u]['Unnamed: 1'].iloc[i]).split()[2]
                    classificacao = str(df[u]['Unnamed: 1'].iloc[i]).split('-')[1]
                else:
                    # verificar se a linha atual começa com um número
                    if str(df[u]['Unnamed: 0'].iloc[i]).split()[0].isdigit():
                        if int(str(df[u]['Unnamed: 0'].iloc[i]).split()[0]) == nr_ref:
                            k = 0
                            nr_ref += 1
                        else:  # a linha atual começa com uma letra
                            k += 1
                            # concatenar o conteúdo da linha atual com o da anterior
                            df[u].loc[i - k, 'Unnamed: 0'] = str(df[u]['Unnamed: 0'].iloc[i - k]) + ' ' + \
                                                              str(df[u]['Unnamed: 0'].iloc[i])
                    else:   # verificar se a linha atual começa com uma letra
                        k += 1
                        # concatenar o conteúdo da linha com a linha anterior
                        df[u].loc[i - k, 'Unnamed: 0'] = str(df[u]['Unnamed: 0'].iloc[i - k]) + ' ' + \
                                                          str(df[u]['Unnamed: 0'].iloc[i])

                    # Cria as colunas Conta Corrente e Classificação para df[0]
                    df[u]['Conta Corrente'].iloc[i] = conta_corrente
                    df[u]['Classificação'].iloc[i] = classificacao

            # Exclui as colunas e linhas desnecessárias
            df[u] = df[u][~df[u].apply(lambda row: row.astype(str).str.contains("Conta contábil").any(), axis=1)]
            df[u] = df[u].dropna(how="any", axis=0)  # excluir linhas parcialmente vazias (NAN)
            df[u] = df[u].dropna(how="any", axis=1)  # excluir colunas parcialmente vazias (NAN)
            df[u] = df[u].reset_index(drop=True)  # reinicia os índices

            # Coloca o df[0] no formato correto
            for i in range(len(df[u])):
                df[u].loc[i, 'NR ORD'] = str(df[u]['Unnamed: 0'].iloc[i]).split()[0]                #
                df[u].loc[i, 'Especificação'] = str(df[u]['Unnamed: 0'].iloc[i]).replace(df[u].loc[i, 'NR ORD'], '',
                                                                                          1).strip()
                df[u].loc[i, 'Nr Ficha'] = str(df[u]['Unnamed: 1'].iloc[i]).split()[0]
                df[u].loc[i, 'Unid Med/ Cons'] = str(df[u]['Unnamed: 1'].iloc[i]).split()[1]
                df[u].loc[i, 'Qtde'] = int(str(df[u]['Unnamed: 1'].iloc[i]).split()[2])
                df[u].loc[i, 'Valor Unitário'] = float(
                    str(df[u]['Unnamed: 2'].iloc[i]).split()[0].replace('.', '').replace(',', '.'))
                df[u].loc[i, 'Valor Total'] = float(
                    str(df[u]['Unnamed: 2'].iloc[i]).split()[1].replace('.', '').replace(',', '.'))
                df[u].loc[i, 'Situação'] = str(df[u]['Unnamed: 2'].iloc[i]).split()[2]
            # Remove as colunas desnecessárias
            df[u] = df[u].drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2'], axis=1)

        else:
            # Junta as demais colunas na coluna 0
            df[u]['Unnamed: 0'] = df[u].apply(lambda row: concatenar_colunas(row), axis=1)

            # Exclui o nan presente na coluna 0
            df[u]['Unnamed: 0'] = df[u]['Unnamed: 0'].apply(lambda row: excluir_nan(row))

            # Preenche as colunas cc e classificação
            for i in range(len(df[u])):
                # Caso a linha inicie por Conta contábil salva os valores de conta-corrente e classificação
                if str(df[u]['Unnamed: 0'].iloc[i]).startswith('Conta'):
                    conta_corrente = str(df[u]['Unnamed: 0'].iloc[i]).split('-')[1].split('corrente:')[1]
                    classificacao = str(df[u]['Unnamed: 0'].iloc[i]).split('-')[2]
                else:
                    df[u].loc[i, ('Conta Corrente')] = conta_corrente
                    df[u].loc[i, ('Classificação')] = classificacao

            # Apaga as linhas que contenham conta contábil
            df[u] = df[u][~df[u].apply(lambda row: row.astype(str).str.contains("Conta contábil").any(), axis=1)]
            df[u] = df[u].reset_index(drop=True)  # reinicia os índices

            # Extrai as infos extras e as coloca nas colunas corretas
            # Seta o nr_ref inicial para df[u]
            nr_ref = int(str(df[u]['Unnamed: 0'].iloc[0]).split()[0])
            for i in range(len(df[u])):
                if str(df[u]['Unnamed: 0'].iloc[i]).split()[0].isdigit():
                    if int(str(df[u]['Unnamed: 0'].iloc[i]).split()[0]) == nr_ref:
                        nr_ref += 1
                        df[u].loc[i, 'NR ORD'] = str(df[u]['Unnamed: 0'].iloc[i]).split()[0]
                        df[u].loc[i, 'Nr Ficha'] = str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][0]
                        df[u].loc[i, 'Unid Med/ Cons'] = str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][1]
                        df[u].loc[i, 'Qtde'] = int(str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][2])
                        df[u].loc[i, 'Valor Unitário'] = float(str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][3].replace('.', '').replace(',', '.'))
                        df[u].loc[i, 'Valor Total'] = float(str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][4].replace('.', '').replace(',', '.'))
                        df[u].loc[i, 'Situação'] = str(df[u]['Unnamed: 0'].iloc[i]).split()[-6:][5]
                        # Elimina as infos extras da coluna Unnamed 0
                        df[u].loc[i, 'Unnamed: 0'] = " ".join(str(df[u]['Unnamed: 0'].iloc[i]).split()[:-6])

            # Junta o conteúdo das linhas da coluna 0 na primeira linha (especificação)
            # Reseta o nr_ref inicial para df[u]
            df[u] = df[u].reset_index(drop=True)  # reinicia os índices
            nr_ref = int(str(df[u]['Unnamed: 0'].iloc[0]).split()[0])
            k = 0
            for i in range(len(df[u])):
                if str(df[u]['Unnamed: 0'].iloc[i]).split()[0].isdigit():  # linha atual começa com um número?
                    if int(str(df[u]['Unnamed: 0'].iloc[i]).split()[0]) == nr_ref:
                        nr_ref += 1
                        k = 0
                    else:  # a linha atual começa com uma letra
                        k += 1
                        # concatenar o conteúdo da linha com a linha anterior
                        df[u].loc[i - k, 'Unnamed: 0'] = str(df[u]['Unnamed: 0'].iloc[i - k]) + ' ' + \
                                                          str(df[u]['Unnamed: 0'].iloc[i])
                else:   # a linha atual começa com uma letra
                    k += 1
                    # concatenar o conteúdo da linha com a linha anterior
                    df[u].loc[i - k, 'Unnamed: 0'] = str(df[u]['Unnamed: 0'].iloc[i - k]) + ' ' + \
                                                     str(df[u]['Unnamed: 0'].iloc[i])

            # Transfere o conteúdo da coluna 0 para a coluna de especificação
            df[u]['Especificação'] = df[u]['Unnamed: 0'].apply(lambda x: ' '.join(str(x).split()[1:]))

            # Remove a colunas e linhas desnecessárias
            df[u] = df[u].drop(['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1)

            # Substituir células vazias por NaN para substituí-las
            df[u].replace("", np.nan, inplace=True)

            # Aplicar dropna para remover as linhas com células vazias na primeira coluna
            df[u] = df[u].dropna(subset=['NR ORD'])

            df[u] = df[u].reset_index(drop=True)  # reinicia os índices

    # Concatena todas os DFs extraídos e formatados num DF único para posterior salvamento em excel
    df_final = pd.concat(df, ignore_index=True)

    # Cálculo da classificação ABC:
    # Ordena o DF por ordem decrscente de valor total
    df_final_ordenado = df_final.sort_values(by='Valor Total', ascending=False)
    df_final_ordenado = df_final_ordenado.reset_index(drop=True)  # reinicia os índices

    # Calcula o valor total do estoque
    valor_total_estoque = round(df_final_ordenado['Valor Total'].sum(), 2)
    print('valor total', valor_total_estoque)

    # Cria colunas adicionais
    # Calcula % individual
    df_final_ordenado['% individual'] = ''
    df_final_ordenado['% individual'] = df_final_ordenado['Valor Total'].apply(lambda x: 100*(x / valor_total_estoque))

    # Calcula % acumulado
    df_final_ordenado['% acumulada'] = ''
    df_final_ordenado.loc[0, '% acumulada'] = df_final_ordenado.loc[0, '% individual']
    soma = df_final_ordenado.loc[0, '% acumulada']
    print(len(df_final_ordenado))
    for i in range(1, len(df_final_ordenado)):
        soma += df_final_ordenado['% individual'].iloc[i]
        df_final_ordenado.loc[i, '% acumulada'] = soma

    # Calcula classificação ABC
    df_final_ordenado['Classificação ABC'] = ''
    df_final_ordenado['Classificação ABC'] = df_final_ordenado['% acumulada'].apply(lambda x: classifica(x))

    # Ajustes finais na tabela
    # Insere informações de valor total do estoque e usuário que emitiu relatório siscomis
    indice = len(df_final_ordenado)
    df_final_ordenado.loc[indice, 'Especificação'] = info_usuario
    df_final_ordenado.loc[indice, 'Valor Unitário'] = 'Valor Total do Estoque'
    df_final_ordenado.loc[indice, 'Valor Total'] = valor_total_estoque
    # Exclui os NaNs presentes na última linha
    df_final_ordenado.loc[indice] = df_final_ordenado.loc[indice].fillna('')
    # Preenche as células vazias das colunas Conta Corrente e Classificação
    df_final_ordenado['Classificação'].fillna('Item sem classificação', inplace=True)
    df_final_ordenado['Conta Corrente'].replace(' ', 'xxx', inplace=True)
    df_final_ordenado.columns = ['NR ORD', 'Especificação', 'Nr Ficha', 'Conta Corrente', 'Classificação',
                                 'Unid Med/ Cons', 'Qtde', 'Valor Unitário', 'Valor Total', 'Situação', '% individual',
                                 '% acumulada', 'Classificação ABC']

    # Salvamento do arquivo excel
    # Caminho para o arquivo Excel resultante
    # caminho_arquivo_excel = "caminho_para_o_arquivo.xlsx"
    # df_final.to_excel(caminho_arquivo_excel, index=False)

    # Nome de salvamento do arquivo
    arquivo_final = f'Inventario Almoxarifado{info_usuario.split(":")[2].replace(", ","_").replace(" ","_")}.xlsx'

    # Rotina que sobreescreve o arquivo caso ele já exista
    try:
        df_salvo = pd.read_excel(arquivo_final)  # Lê o dataframe
        df_salvo = df_final_ordenado  # Faz as alterações no dataframe
        df_salvo.to_excel(arquivo_final, index=False)  # Salva o DataFrame como um arquivo Excel
    except:
        df_final_ordenado.to_excel(arquivo_final, index=False)  # Salva o DataFrame como um arquivo Excel

# #####################################################################################
#     # Reabrir o arquivo Excel
#     df_salvo = pd.read_excel(arquivo_final)
#     workbook = load_workbook(arquivo_final)
#
#     # Especificar a planilha que você deseja alterar
#     sheet = workbook.active
#
#     # Configurar a largura das colunas
#     largura_colunas = {'A': 15, 'B': 20, 'C': 25}  # Exemplo: largura de 15 para a coluna A, 20 para a coluna B, etc.
#
#     for col, width in largura_colunas.items():
#         sheet.column_dimensions[col].width = width
#
#     # Configurar o alinhamento das células
#     alinhamento_colunas = {'A': 'center', 'B': 'left',
#                            'C': 'right'}  # Exemplo: alinhamento centralizado para a coluna A, alinhado à esquerda para a coluna B, etc.
#
#     for col, alignment in alinhamento_colunas.items():
#         for cell in sheet[col]:
#             cell.alignment = Alignment(horizontal=alignment)
#
#     # Salvar o arquivo Excel modificado
#     workbook.save(arquivo_final)


    # try:
    #     df_salvo = pd.read_excel(arquivo_final)  # Lê o dataframe
    #     df_salvo = df_final_ordenado
    #     df_salvo.to_excel(arquivo_final, index=False)  # Salva o DataFrame como um arquivo Excel
    # except:
    #     df_final.to_excel(arquivo_final, index=False)
    #     #salva_arquivo(df_salvo, arquivo_final)

    #configura_arquivo(arquivo_final)


if __name__ == '__main__':
    conversao("Inventário de Almoxarifado 26.06.pdf")
