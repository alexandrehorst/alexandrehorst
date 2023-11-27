#!/usr/bin/env python
# coding: utf-8

# In[8]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time, os
import urllib.request
from credentials import user, password


# Função que verifica se determinado diretório exsite 
def verifica_e_cria_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f'Diretório {diretorio} criado com sucesso.')
    else:
        print(f'O diretório {diretorio} já existe.')      


# Diretórios para salvamento das fotos        
dir_mat1 = 'C:\\Users\\Alexandre\\Downloads\\Fotos Viva\\Mat1'
dir_pre2 = 'C:\\Users\\Alexandre\\Downloads\\Fotos Viva\\Pre2'
        
# Cria diretórios para salvamentos das fotos
verifica_e_cria_diretorio(dir_mat1)
verifica_e_cria_diretorio(dir_pre2)

# Abre o navegador no site
url = 'https://online.vivasistemas.com/login'
navegador = webdriver.Chrome()
navegador.get(url)
time.sleep(10)

# Encontre o campo de login e insira o login
login_input = navegador.find_element('xpath', '//*[@id="email"]')
login_input.send_keys(user)

# Encontre o campo de senha e insira a senha
senha_input = navegador.find_element('xpath', '//*[@id="password"]')
senha_input.send_keys(password)

# Envie o formulário (pode ser um clique em um botão de login também, dependendo do site)
senha_input.send_keys(Keys.ENTER)
time.sleep(10)
# Seleciona Beatriz e Guilherme (xpath do botão selecionado)
xpath_filhos = ['/html/body/app-root/app-filhos/div/div[2]/div/div/div[2]/div/div[2]/button', '/html/body/app-root/app-filhos/div/div[2]/div/div/div[3]/div/div[2]/button']

count = 0
for xp in xpath_filhos:
    # Depois de baixar a fotos do primeiro filho retorna para o menu inicial
    if count == 1:
        # Clica no link Filhos
        #navegador.find_element('xpath', '//*[@id="side-menu"]/li[2]/a').click()
        navegador.find_element('xpath', '//*[@id="side-menu"]/li[2]/a/span').click()
        time.sleep(20)
    
    seleciona_filho = navegador.find_element('xpath', xp).send_keys(Keys.ENTER)
    time.sleep(30)

    # Clica no link portifólio
    seleciona_portifolio = navegador.find_element('xpath', '//*[@id="side-menu"]/li[5]/a/span').click()
    time.sleep(30)

    # Encontre todos os elementos de link da página:
    elementos_img = navegador.find_element(By.TAG_NAME, "app-root")

    # Verificar o que há dentro do WebElement
    #conteudo_elemento = elementos_img.get_attribute("innerText") # Formato Texto
    conteudo_elemento = elementos_img.get_attribute("innerHTML") # Formato HTML
    time.sleep(30)

    # Cria um objeto BeautifulSoup com o conteúdo HTML
    soup = BeautifulSoup(conteudo_elemento, "html.parser")

    # Busca todos os links de imagens dentro do WebElement
    links_imagens = soup.find_all("img")
    print(len(links_imagens)) # quantidade de fotos do link

    timeout = 120
    # Percorre a lista com os links e baixa todas as fotos 
    for link in links_imagens:
        url = link.get("src")
        print(link.get("src"))
        # Abre a URL com um timeout
        if url.startswith('https:'):
            try:
                # Extrai o nome da imagem do URL
                nome_arquivo = url.split("/")[-1]
                response = urllib.request.urlopen(url, timeout=timeout)
                # Se a solicitação for bem-sucedida, baixe o arquivo                
                if count == 0:  # Separa os diretórios nos quais as fotos serão salvas
                    # Caso o arquivo não exista dentro do diretório, o arquivo será salvo
                    if not os.path.isfile(f'{dir_mat1}\\{nome_arquivo}'):
                        with open(f'{dir_mat1}\\{nome_arquivo}', 'wb') as file:
                            file.write(response.read())
                        print(f"{nome_arquivo} baixado com sucesso!")
                else:
                    # Caso o arquivo não exista dentro do diretório, o arquivo será salvo
                    if not os.path.isfile(f'{dir_pre2}\\{nome_arquivo}'):
                        with open(f'{dir_pre2}\\{nome_arquivo}', 'wb') as file:
                            file.write(response.read())
                        print(f"{nome_arquivo} baixado com sucesso!")                
            except urllib.error.URLError as e:
                print(f"Erro de URL: {e.reason}")
            except socket.timeout:
                print("Tempo limite de solicitação atingido. A conexão foi interrompida.")
    count += 1
    time.sleep(15)

# Fecha o navegador
navegador.quit()

print('Download das fotos concluído!')


# In[ ]:





# In[ ]:




