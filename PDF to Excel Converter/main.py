import tkinter as tk  # importa todo módulo Tkinter
from tkinter.filedialog import askopenfilename
from conversor_pdf_excel import *
from PIL import Image, ImageTk
from conversor_pdf_excel_rel_mat_perm import *

print(tk.TkVersion)

caminho_arquivo = ''


# Função que abre uma janela para selecionar o arquivo desejado
def selecionar_arquivo():
    global caminho_arquivo
    try:
        caminho_arquivo = askopenfilename(title="Selecione um arquivo em Excel para abrir")
        if caminho_arquivo.endswith('.pdf'):
            msg_caminho_arquivo_entrada['text'] = caminho_arquivo
            return caminho_arquivo
        else:
            msg_caminho_arquivo_entrada['text'] = 'Arquivo inválido!'
            return None
    except:
        msg_caminho_arquivo_entrada['text'] = 'Arquivo inválido!'
        return None


def converter_arquivo(caminho_arquivo_pdf):
    global caminho_arquivo
    if caminho_arquivo:
        try:
            conversao(caminho_arquivo_pdf=caminho_arquivo)
        except:
            conversao_rel_mat_perm(nome_arquivo=caminho_arquivo)
        msg_arquivo_atualizado['text'] = 'Arquivo em excel gerado com sucesso!'
    else:
        msg_arquivo_atualizado['text'] = 'Nenhum arquivo selecionado!'


def abrir_janela_sobre():
    janela_sobre = tk.Toplevel(janela)
    janela_sobre.geometry("600x250")
    janela_sobre.title("Sobre o programa")
    janela_sobre.configure(bg='#b0e0e6')
    janela_sobre.resizable(False, False)

    # Adiciona texto à caixa de texto
    texto = """
    Versão 2.0
    Este programa criado exclusivamente para transformar o relatório de INVENTÁRIO DE ALMOXARIFADO POR DEPÓSITO e o 
    relatório de material permanente ambos gerados pelo SISCOFIS e não foi testado para outros arquivos em PDF.
    Para converter o arquivo PDF para excel siga os seguintes passos:
    1- Selecione o arquivo em formato  excel desejado (será mostrado o diretório contendo o mesmo).
    2- Clique em "Converter arquivo".
    3- O arquivo em excel será gerado na mesma pasta onde se encontra o arquivo executável.
    4- Clique em fechar para encerrar o programa.
    
    Para informar bugs ou retirar dúvidas, envie um e-mal para horstmann.alexandre@eb.mil.br
    """

    label = tk.Label(janela_sobre, text=texto, fg='black', bg='#b0e0e6', justify='left')
    label.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky="NSEW")

    botao_fechar = tk.Button(janela_sobre, text="Fechar", bg='#b0e0e6', command=janela_sobre.destroy)
    botao_fechar.grid(row=5, column=0, padx=10, pady=10, sticky="NSEW")


# inicia janela
janela = tk.Tk()
janela.geometry("800x300")  # Defina as dimensões da janela

# Insere título da janela
janela.title("Conversor do Relatório de Inventário do SISCOFIS do formato PDF para Excel")

# Configura a cor do backgorund da janela
janela.configure(bg='#b0e0e6')

# Prepara imagem a ser inserida na janela #####################################
# Carrega a imagem usando a biblioteca PIL
imagem_pil = Image.open("banner_logo.png")
largura_original, altura_original = imagem_pil.size

# Ajuste a largura máxima desejada da imagem
largura_maxima = 780
proporcao = largura_maxima / float(largura_original)
altura_desejada = int(altura_original * proporcao)

# Redimensione a imagem
imagem_redimensionada = imagem_pil.resize((largura_maxima, altura_desejada), Image.BILINEAR)

# Converte a imagem para o formato PhotoImage
imagem = ImageTk.PhotoImage(imagem_redimensionada)

# Cria um Label com a imagem e a posicione na janela
label_imagem = tk.Label(janela, image=imagem, anchor='center')
label_imagem.grid(row=0, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

####################################################################################################################
# Seleciona arquivo
msg_selecionar_arquivo = tk.Label(text="Selecione o arquivo em PDF que deseja converter para Excel:", fg='black',
                                       bg='#b0e0e6')
msg_selecionar_arquivo.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Botão para selecionar o arquivo
bt_selecionar_arquivo = tk.Button(text="Clique aqui para selecionar", fg='black', bg='#b0e0e6',
                                  command=selecionar_arquivo)
bt_selecionar_arquivo.grid(row=1, column=1, padx=10, pady=10)  # Adiciona o botão na janela

# Caminho do arquivo
msg_caminho_arquivo_entrada = tk.Label(text="Nenhum arquivo selecionado", fg='black', bg='#b0e0e6')
msg_caminho_arquivo_entrada.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="NS")

# Botão para executar conversão do arquivo
bt_converter_arquivo = tk.Button(text="Converter arquivo", fg='black', bg='#b0e0e6',
                                 command=lambda: converter_arquivo(caminho_arquivo))
bt_converter_arquivo.grid(row=2, column=1, padx=10, pady=10)  # Adiciona o botão na janela

# Msg de arquivo atualizado
msg_arquivo_atualizado = tk.Label(text="", fg='black', bg='#b0e0e6', anchor='n')
msg_arquivo_atualizado.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="NSEW")

# Botão para abrir janela sobre o programa
botao_fechar_programa = tk.Button(text="Sobre o programa", fg='black', bg='#b0e0e6', command=abrir_janela_sobre)
botao_fechar_programa.grid(row=4, column=0, padx=10, pady=10)  # Adiciona o botão na janela

# Botão para fechar programa
botao_fechar_programa = tk.Button(text="Fechar", fg='black', bg='#b0e0e6', command=janela.quit)
botao_fechar_programa.grid(row=4, column=1, padx=10, pady=10)  # Adiciona o botão na janela

# Roda o código continuamente permitindo que a janela fique continuamente na tela
janela.resizable(True, False)
janela.mainloop()
