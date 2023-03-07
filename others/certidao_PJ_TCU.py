# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 21:00:31 2022

@author: Alexandre
"""
import pyautogui as auto

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

import time

# Certidão Consolidada de PJ no TCU
#Acessa a página do TCU
navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://certidoes-apf.apps.tcu.gov.br/"
navegador.get(link)

#Seta o xpatch do campo de buscas:
search_box = navegador.find_element(By.XPATH,'/html/body/app-root/div/ng-component/div/div/div[1]/div[2]/div/\
                                    div[1]/input')

#Escreve o CNPJ no campo de buscas                               
search_box.send_keys('00.435.091/0001-98')

#Seta o xpatch do botão para executar a busca:
search_buttom = navegador.find_element(By.XPATH,'/html/body/app-root/div/ng-component/div/div/div[1]/div[2]/div/\
                                       div[2]/button')

#Pressiona o botão para executar a pesquisa
search_buttom.click()

#Seta o xpatch do botão para baixar a certidão:
time.sleep(5)
search_buttom = navegador.find_element(By.XPATH,'/html/body/app-root/div/ng-component/div/div/div[2]/div/div[2]\
                                       /div/button')
#Pode ser usado também o cmdo "xpath" ao invés de By.XPATH

#Pressiona o botão para executar o download
search_buttom.click()