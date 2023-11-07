from flask_bcrypt import Bcrypt
from tkinter import *
import pyodbc
import time
from getpass import getpass
import logging


def fazer_login():
    global entry0, entry1, entry2, entry3, entry4, login
    login = entry_usuario.get()
    senha = entry_senha.get()
    bcrypt = Bcrypt()
    if login and senha:
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM users WHERE Username='{login}'")
        valores = cursor.fetchall()
        print(valores)
        cursor.close()  
        conexao.close()
        bcrypt.check_password_hash(valores[0][1], senha)
        if valores != []:
            if bcrypt.check_password_hash(valores[0][1], senha):    
                print('Credenciais válidas')
                janela_login.destroy()  # fecha janela de login
                abrir_janela_principal()  # abre segunda janela        
            else:            
                label_erro["text"] = "Login e/ou senha incorretos"  # Exibe mensagem de erro
    else:            
        print('Usuário e/ou senha não preenchidos!')
        label_erro["text"] = "Login e/ou senha incorretos"  # Exibe mensagem de erro
        

# Limpa os campos de entrada 
def resetar_campos():
    entry0.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
        
    
def usar_insumo():
    entry4.delete("1.0", END)  # Apaga a área de texto
    # Pega o código de estoque e quantidade do insumo que será utilizado
    qtd = entry1.get()  # Pega todas as infos do insumo para atualizar o BD
    cod_estoque = entry3.get().strip()
    # localizar o insumo no BD e atualizar a qtd
    # mostrar infos do insumo atualizada na caixa de texto (entry4)
    # Se a qtd e código de estoque (infos necessárias) tiverem sido informadas, realiza a operação 
    if qtd and cod_estoque:
        qtd = float(qtd)
        # Faz a conexão com o BD
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM estoque WHERE CodigoEstoque='{cod_estoque}'")
        valores = cursor.fetchall()  # Pega todos os valores da tabela 
        # Encerra a conexão
        cursor.close()  
        conexao.close()
        time.sleep(1)
        if (valores[0][2] > 0) and (valores[0][2] >= qtd):
            # Atualiza o BD
            nova_qtd = valores[0][2] - qtd
            dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            cursor.execute(f"""
            UPDATE estoque SET Quantidade='{nova_qtd}' WHERE CodigoEstoque='{cod_estoque}'""") 
            cursor.commit() # # Salva as alterações no BD (faz um commit)
            cursor.close()
            conexao.close() # finaliza a conexão
            entry4.insert(END, 'Estoque atualizado!\n')
            entry4.insert(END, f'Insumo: {valores[0][0]}\nCódigo de estoque: {valores[0][1]}\n'
                f'Quantidade: {nova_qtd}\nValidade: {valores[0][3]}\n\n')
            # Registra a operação no log
            logging.info(f"Operação: [Procura insumo], Usuário: {login}, Insumo: {valores[0][0]}, \
            Código de Estoque: {valores[0][1]}, Quantidade utilizada: {qtd}, Nova Quantidade: {nova_qtd}, \
            Validade: {valores[0][3]}")
            # Limpa campos de entrada antes de realizar uma operação
            resetar_campos()
        else:
            entry4.insert(END, 'Não foi possível realizar a operação!\nItem zerado no estoque ou a quantidade'
                          'informada é maior do que a quantidade disponível!')            
    else:
        entry4.insert(END, 'Não foi possível realizar a operação!\nFavor verificar se a quantidade e o código do ' 
                      'insumo foram inseridos.') 
    

""" O usuário insere todas as infos do insumo e, caso não haja nenhum registro com o mesmo nome ou código de estoque,
o item será adicionado"""
def adicionar_insumo(): 
    entry4.delete("1.0", END)  # Apaga a área de texto
    # Pega as infos do insumo para adicionar ao BD
    validade = entry0.get().strip() 
    qtd = entry1.get()
    insumo = entry2.get().strip()
    cod_estoque = entry3.get().strip()
    if insumo and cod_estoque and qtd:
        # Verifica se o nome e o código de estoque do insumo já estão cadastrados no BD
        # Faz a conexão com o BD
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")        
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        cursor.execute(f"SELECT * FROM estoque WHERE Insumo='{insumo}' or CodigoEstoque='{cod_estoque}'")
        valores = cursor.fetchall()  # Pega todos os valores da tabela    
        print(valores)
        # Encerra a conexão
        cursor.close()  
        conexao.close()
        time.sleep(1)
        if valores == []:
            dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            # Insere as infos no BD
            cursor.execute(f"""
            INSERT INTO estoque (Insumo, CodigoEstoque, Quantidade, Validade) 
            VALUES ('{insumo}', '{cod_estoque}', '{qtd}', '{validade}')
            """)
            cursor.commit()  # Salva as alterações no BD (faz um commit)
            # Exibe msg para o usuário
            entry4.insert(END, f'Adicionando {insumo} ao estoque.\nCódigo de estoque: {cod_estoque}\n'
            f'Validade: {validade}\nQuantidade: {qtd}')
            # Encerra a conexão
            cursor.close()  
            conexao.close()
            # Registra a operação no log
            logging.info(f"Operação: [Inclusão de insumo], Usuário: {login}, Insumo: {insumo}, \
            Código de Estoque: {cod_estoque}, Validade: {validade}, Quantidade: {qtd}")
            # Apaga os campos de entrada para a realização de uma nova operação com o BD
            resetar_campos()
        else:
            # Exibe msg para o usuário
            entry4.insert(END, 'Já há cadastro com o código de estoque especificado!')
            # Registra a operação no log
            logging.info(f"Operação: [Tentativa de inclusão de insumo repetido], Usuário: {login}, Insumo: {insumo}, \
            Código de Estoque: {cod_estoque}, Validade: {validade}, Quantidade: {qtd}")            
    else:
        entry4.insert(END, 'Não foi possível realizar a operação!\nFavor verificar se a quantidade, o nome e o código do ' 
                      'insumo foram inseridos.') 
    
    
# O usuário insere o nome ou código de estoque do insumo e a busca retorna todos os resultados encontrados no BD    
def procurar_insumo():    
    entry4.delete("1.0", END)  # Apaga a área de texto
    insumo = entry2.get().strip()  # Pega as infos para realizar a busca
    cod_estoque = entry3.get().strip()
    # Se não forem especificados nem o nome nem o código de estqoue do insumo, serão mostrados todos os itens que estão no BD
    # Faz a conexão com o BD
    dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    # Realiza uma consulta ao BD para buscar o insumo        
    if cod_estoque:  # Busca pelo código de estoque (pesquisa específica)           
        cursor.execute(f"SELECT * FROM estoque WHERE CodigoEstoque='{cod_estoque}'")   
    else: # Busca pelo nome do insumo (pesquisa genérica)
        cursor.execute(f"SELECT * FROM estoque WHERE Insumo LIKE '%{insumo}%'")          
    valores = cursor.fetchall()  # Pega todos os valores da tabela
    print(valores)        
    cursor.close()
    conexao.close()
    if valores == []:  # Mostra msg ao usuário indicando o resultado da busca
        entry4.insert(END,'Não foi possível localizar nenhum insumo com o código e nome informado!')
    else:        
         entry4.insert(END, f'Resultado da Busca:\n') 
         for busca in valores:
             # Exibe msg para o usuário na área de texto
             entry4.insert(END, f'Insumo: {busca[0]}\nCódigo de estoque: {busca[1]}\n'
             f'Quantidade: {busca[2]}\nValidade: {busca[3]}\n\n')
             # Registra a operação no log
             logging.info(f"Operação: [Procura insumo], Usuário: {login}, Insumo: {busca[0]}, \
             Código de Estoque: {busca[1]}, Quantidade: {busca[2]}, Validade: {busca[3]}")
         # Apaga os campos de entrada para a realização de uma nova operação com o BD
         resetar_campos()    
    return valores    
    
        
def abrir_sub_janela():
    global sub_janela, botao_selecionado, window    
    sub_janela = Tk()
    sub_janela.title("Deseja excluir item")
    sub_janela.geometry("250x60")
    mensagem = Label(sub_janela, text="Deseja mesmo excluir o insumo selecionado?")
    mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")
    # Cria um botão para buscar a info (text: texto do botão e command: função que será executada)
    botao_sim = Button(sub_janela, text="SIM", command=lambda: selecionar_botao('SIM'))
    botao_sim.grid(row=1, column=0) # Adiciona o botão na janela
    botao_nao = Button(sub_janela, text="NÃO", command=lambda: selecionar_botao('NÃO'))
    botao_nao.grid(row=1, column=1) # Adiciona o botão na janela

    
def selecionar_botao(botao):
    global botao_selecionado
    botao_selecionado =  botao
    sub_janela.destroy()
    
    
def deletar_insumo():
    global botao_selecionado
    botao_selecionado = None
    entry4.delete("1.0", END) # Apaga a área de texto
    cod_estoque = entry3.get().strip()  # Pega o código de estoque do insumo a ser retirado
    if cod_estoque:
        # Faz a conexão com o BD
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        abrir_sub_janela()
        sub_janela.wait_window()
        retorno_busca = procurar_insumo()
        entry4.delete("1.0", END) # Apaga a área de texto
        if botao_selecionado == 'SIM':
            # Busca e deleta o insumo do BD
            cursor.execute(f"""DELETE FROM estoque WHERE CodigoEstoque='{cod_estoque}'""")
            cursor.commit()  # Salva as alterações no BD (faz commit)            
            # exibir uma msg dizendo que deletou o insumo do BD
            entry4.insert(END, f'Insumo com código de estoque {cod_estoque} excluído do almoxarifado!')
        # Encerra a conexão  
        cursor.close()
        conexao.close()        
        # Registra a operação no log
        logging.info(f"Operação: [Exclusão de insumo], Usuário: {login}, Insumo: {retorno_busca[0][0]}, \
        Código de estoque: {retorno_busca[0][1]}, Validade = {retorno_busca[0][3]}, Quantidade: {retorno_busca[0][2]}")
        # Apaga os campos de entrada para a realização de uma nova operação com o BD
        resetar_campos()
    else:
        entry4.insert(END, f'Favor informar um código de estoque para realizar esta operação!')


def abrir_janela_principal():
        global entry0, entry1, entry2, entry3, entry4, botao_selecionado, sub_janela, window, b0 
        # Inicia o log
        logging.basicConfig(filename='log_db.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        # Criação da interface gráfica do programa    
        window = Tk()
        
        window.title('Sistema de Controle de Estoque')  # Título da janela
        window.geometry("448x750")
        window.configure(bg = "#ffffff")

        canvas = Canvas(window, bg = "#ffffff", height = 750, width = 448, bd = 0, highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background.png")
        background = canvas.create_image(224.0, 375.0, image=background_img)

        # Validade
        entry0_img = PhotoImage(file = f"img_textBox0.png")
        entry0_bg = canvas.create_image(298.0, 525.0, image = entry0_img)

        entry0 = Entry(bd = 0, bg = "#fffdfd", highlightthickness = 0)
        entry0.place(x = 160, y = 509, width = 276, height = 30)

        # Quantidade
        entry1_img = PhotoImage(file = f"img_textBox1.png")
        entry1_bg = canvas.create_image(297.0, 572.0, image = entry1_img)

        entry1 = Entry(bd = 0, bg = "#fffdfd", highlightthickness = 0)
        entry1.place(x = 159, y = 556, width = 276, height = 30)

        # Insumo
        entry2_img = PhotoImage(file = f"img_textBox2.png")
        entry2_bg = canvas.create_image(298.0, 431.0, image = entry2_img)

        entry2 = Entry(bd = 0, bg = "#fffdfd", highlightthickness = 0)
        entry2.place(x = 160, y = 415, width = 276, height = 30)

        # Código de estoque
        entry3_img = PhotoImage(file = f"img_textBox3.png")
        entry3_bg = canvas.create_image(297.0, 478.0, image = entry3_img)

        entry3 = Entry(bd = 0, bg = "#fffdfd", highlightthickness = 0)
        entry3.place(x = 159, y = 462, width = 276, height = 30)

        entry4_img = PhotoImage(file = f"img_textBox4.png")
        entry4_bg = canvas.create_image(223.5, 656.0, image = entry4_img)

        # Campo para exibir o produto do banco de dados
        entry4 = Text(bd = 0, bg = "#fffdfd", highlightthickness = 0)
        entry4.place(x = 11, y = 610, width = 425, height = 90)

        # Procurar insumo
        img0 = PhotoImage(file = f"img0.png")
        b0 = Button(image = img0, borderwidth = 0, highlightthickness = 0, command = procurar_insumo, relief = "flat")
        b0.place(x = 256, y = 342, width = 157, height = 31)

        # Deletar insumo
        img1 = PhotoImage(file = f"img1.png")
        b1 = Button(image = img1, borderwidth = 0, highlightthickness = 0, command = deletar_insumo, relief = "flat")
        b1.place(x = 40, y = 342, width = 157, height = 31)

        # Adicionar insumo
        img2 = PhotoImage(file = f"img2.png")
        b2 = Button(image = img2, borderwidth = 0, highlightthickness = 0, command = adicionar_insumo, relief = "flat")
        b2.place(x = 40, y = 296, width = 157, height = 31)

        # Registrar uso insumo
        img3 = PhotoImage(file = f"img3.png")
        b3 = Button(image = img3, borderwidth = 0, highlightthickness = 0, command = usar_insumo, relief = "flat")
        b3.place(x = 256, y = 296, width = 157, height = 31)

        window.resizable(False, False)
        window.mainloop()

janela_login = Tk()
janela_login.title("Login")
janela_login.geometry("250x150")

# Elementos da janela de login
label_usuario = Label(janela_login, text="Usuário:")
label_usuario.pack()
entry_usuario = Entry(janela_login)
entry_usuario.pack()

label_senha = Label(janela_login, text="Senha:")
label_senha.pack()
entry_senha = Entry(janela_login, show="*")
entry_senha.pack()

button_login = Button(janela_login, text="Login", command=fazer_login)
button_login.pack()

label_erro = Label(janela_login, text="")
label_erro.pack()

# Loop principal da janela de login
janela_login.mainloop()