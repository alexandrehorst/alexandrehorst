from flask_bcrypt import Bcrypt
import pyodbc
from getpass import getpass

bcrypt = Bcrypt()

nome_usuario = input('Insira um nome de usuário: ')
# Verifica se há usuário cadastrado
if nome_usuario:  # Se o nome do usuário for especificado, realiza a busca
        # Faz a conexão com o BD
        dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
        # Realiza uma consulta ao BD para buscar o usuário
        cursor.execute(f"SELECT * FROM users WHERE Username='{nome_usuario}'")        
        valores = cursor.fetchall()  # Pega todos os valores da tabela            
        cursor.close()
        conexao.close()
        if valores == []:  # Mostra msg ao usuário indicando o resultado da busca
            senha = getpass('Insira uma senha para cadastro: ')
            # Gera o hash da senha
            senha_cript = bcrypt.generate_password_hash(senha).decode('utf-8')
            print(senha_cript)
            # Faz a conexão com o BD 
            dados_conexao = ("Driver={SQLite3 ODBC Driver};Server=localhost;Database=almoxarifado.db")
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            # Salva as infos de usuáro e senha (hash) no BD
            cursor.execute(f"""
            INSERT INTO users (Username, Password) 
            VALUES ("{nome_usuario}", "{senha_cript}")
            """)            
            cursor.commit()  # Salva as alterações no BD (faz um commit)
            # Encerra a conexão
            cursor.close()  
            conexao.close()
            print(f'Usuário {nome_usuario} cadastrado com sucesso')
            # Verificar se o hash da senha está correto
            bcrypt.check_password_hash(senha_cript, senha)
        else:
            print('Usuário já cadastrado!')
        
else:
    print('É necessário informar um nome de usuário!')