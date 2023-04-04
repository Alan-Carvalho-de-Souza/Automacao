# automação web com selenium, pyautogui e pandas

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pyautogui as pa


navegador = webdriver.Chrome()


# Passo 1: Pegar cotação do dolar

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
valor_dolar = float(cotacao_dolar)

# Passo 2: Pegar cotação do euro

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
valor_euro = float(cotacao_euro)

# Passo 3: Pegar cotação do bitcoin

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação bitcoin")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_bitcoin = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
valor_bitcoin = float(cotacao_bitcoin)

# Passo 4: Ordenar numa tabela os valores coletados
moedas = {
    'moeda': ['Bitcoin', 'Dólar', 'Euro'],
    'valores': [valor_bitcoin, valor_dolar, valor_euro]
}
dataframe = pd.DataFrame(moedas)
print(dataframe)

# Passo 5: Gerar um arquivo Excel

dataframe.to_excel('moedas.xlsx', index=False)
# Passo 6: Enviar o arquivo via e-mail
