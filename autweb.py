# automação web com selenium, pyautogui e pandas

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pyautogui as pa
import pyperclip
import time


navegador = webdriver.Chrome()


# Passo 1: Pegar cotação do dolar

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dolar")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


# Passo 2: Pegar cotação do euro

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')


# Passo 3: Pegar cotação do bitcoin

#navegador.get('https://www.google.com.br/')
#navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação bitcoin")
#navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
#cotacao_bitcoin = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('pclqee')


# Passo 4: Ordenar numa tabela os valores coletados
#valor_bitcoin = float(cotacao_bitcoin)
#print(valor_bitcoin)
valor_dolar = float(cotacao_dolar)
valor_euro = float(cotacao_euro)
print(valor_dolar)
print(valor_euro)

moedas = ['Dólar', 'Euro']
valores = [valor_dolar, valor_euro]

dataframe = pd.DataFrame({
    'Moeda': moedas,
    'Valor': valores

})

print(dataframe)

# Passo 5: Gerar um arquivo Excel

dataframe.to_excel('moedas.xlsx', index=False)
# Passo 6: Enviar o arquivo via e-mail

descricao_email = f'''Prezado, bom dia.

Segue relatório da cotação de moedas, referente ao dia anterior.

Qualquer dúvida estou à disposição.
Atenciosamente.'''

pa.press('win')
time.sleep(2)
pa.write('chrome')
pa.press('enter')
time.sleep(2)
pa.hotkey('ctrl', 'shift', 'n')
time.sleep(3)
pa.write('gmail.com')
pa.press('enter')
time.sleep(6)
pa.click(x=552, y=363)
time.sleep(2)
pa.write('alan.carvalhodesouza96@gmail.com') # usuário de email
time.sleep(1)
pa.press('enter')
time.sleep(3)
pa.write('#Devautomacao2023#') #senha do e-mail
pa.press('enter')
time.sleep(2)
pa.click(x=69, y=197)

time.sleep(4)
pa.write('automacoes.2023@gmail.com')
pa.press('tab')
time.sleep(2)
pa.write('negociolojaonline.01@gmail.com')
pa.press('tab')
time.sleep(4)
pa.press('tab')
time.sleep(3)
pyperclip.copy('Teste de automação 11') # Quando houver caracter especial utilizar pyperclip.copy
pa.hotkey('ctrl', 'v')
time.sleep(2)
pa.press('tab')

pyperclip.copy(descricao_email)
pa.hotkey('ctrl', 'v')
time.sleep(2)
pa.click(x=964, y=702)
time.sleep(1)

pa.click(x=382, y=641)
pasta = f'''C:\Automacao'''
pyperclip.copy(pasta)
time.sleep(1)
pa.press('enter')
time.sleep(2)
pa.click(x=359, y=420)
time.sleep(1)
pyperclip.copy('moedas')
time.sleep(1)
pa.hotkey('ctrl', "v")
pa.press('enter')
time.sleep(3)
pa.click(x=837, y=702)
"""
navegador.find_element('xpath', '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('#Devautomacao2023#')
navegador.find_element('xpath', '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div/div').click()
navegador.find_element('xpath', '//*[@id=":u4"]').send_keys('automacoes.2023@gmail.com')
navegador.find_element('xpath', '//*[@id=":u4"]').send_keys(Keys.TAB)
navegador.find_element('xpath', '//*[@id=":u4"]').send_keys(Keys.TAB)
navegador.find_element('xpath', '//*[@id=":q6"]').send_keys('Cotação de Moeda - 05.04.2023')
navegador.find_element('xpath', '//*[@id=":q6"]').send_keys(Keys.TAB)
pyperclip.copy(descricao_email)
pa.hotkey('ctrl', 'v')
navegador.find_element('xpath', '//*[@id=":pw"]').click()
"""
print('Seu e-mail foi enviado com sucesso!')