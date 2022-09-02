#Inserir senha utilizando cadeia de caracteres repetida com comprimento especificado em 6


from selenium import webdriver
import time

from selenium.webdriver.common.by import By

drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
drive.get('https://mateusmais.com.br/cadastro')
drive.maximize_window()

senha = 'aaaaaa'
confsenha = 'aaaaaa'

campoSenha = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input:nth-child(7) > div > div.input-wrapper.normal.-has-icon > input")
time.sleep(1)
campoSenha.send_keys(senha)

campoConfSenha = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input:nth-child(8) > div > div > input")
time.sleep(1)
campoConfSenha.send_keys(confsenha)

botao_entrar = drive.find_element(By.CSS_SELECTOR,"body > app-root > app-master-page > app-register > div > div > div > gmf-button > div > button > div.content.--gmf-text > div")
time.sleep(1)
botao_entrar.click()