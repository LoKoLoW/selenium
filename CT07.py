#Inserir letras e caracteres especiais no campo data de nascimento

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
drive.get('https://mateusmais.com.br/cadastro')
drive.maximize_window()

dataNasc = 'junior**'


campoNasc = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-datepicker > div > div > input")
time.sleep(1)
campoNasc.send_keys(dataNasc)

botao_entrar = drive.find_element(By.CSS_SELECTOR,"body > app-root > app-master-page > app-register > div > div > div > gmf-button > div > button > div.content.--gmf-text > div")
time.sleep(1)
botao_entrar.click()