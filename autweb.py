# automação web com selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

# Passo 1: Pegar cotação do dolar

navegador.get('https://www.google.com.br/')

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")

navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
