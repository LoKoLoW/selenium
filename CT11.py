#Inserir email inválido com formatação padrão de email @. (aaa@aaa.aaa)


from selenium import webdriver
import time

from selenium.webdriver.common.by import By

drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
drive.get('https://mateusmais.com.br/cadastro')
drive.maximize_window()

email = 'aaa@aaa.aaa'
confEmail = 'aaa@aaa.aaa¨'

campoEmail = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input:nth-child(5) > div > div.input-wrapper.normal.-has-icon > input")
time.sleep(1)
campoEmail.send_keys(email)

campoConfEmail = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input:nth-child(6) > div > div.input-wrapper.normal.-has-icon > input")
time.sleep(1)
campoConfEmail.send_keys(confEmail)

botao_entrar = drive.find_element(By.CSS_SELECTOR,"body > app-root > app-master-page > app-register > div > div > div > gmf-button > div > button > div.content.--gmf-text > div")
time.sleep(1)
botao_entrar.click()