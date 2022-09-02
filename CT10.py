#Inserir CPF gerado aleatoriamente

from selenium import webdriver
import time
import random

from selenium.webdriver.common.by import By

drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
drive.get('https://mateusmais.com.br/cadastro')
drive.maximize_window()
lol = (random.random())
cpf = lol


campoCPF = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input:nth-child(4) > div > div > input")
time.sleep(1)
campoCPF.send_keys(cpf)

botao_entrar = drive.find_element(By.CSS_SELECTOR,"body > app-root > app-master-page > app-register > div > div > div > gmf-button > div > button > div.content.--gmf-text > div")
time.sleep(1)
botao_entrar.click()