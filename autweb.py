# automação web com selenium

from selenium import webdriver

navegador = webdriver.Chrome()

# Passo 1: Pegar cotação do dolar

navegador.get('https://www.google.com.br/')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').click