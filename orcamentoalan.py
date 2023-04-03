"""
Testando conhecimentos de automação de tarefas

Objetivo criar uma automação, para enviar uma planilha com os dados de orçamento pessoal via e-mail
"""
# Código para rodar no notebook pessoal
# Configurações de posições de acordo com meu notebook

import pandas as pd
import pyautogui as pa
import time
import pyperclip

#time.sleep(5)
#print(pa.position())


pa.click(x=514, y=750)
time.sleep(2)
pa.write('gmail.com')
pa.press('enter')
time.sleep(3)
pa.click(x=75, y=207)
time.sleep(3)
pa.write('alan_carvalho_96@hotmail.com')
pa.press('tab')
time.sleep(3)
pa.press('tab')
time.sleep(2)
pyperclip.copy('Teste de automação 5') # Quando houver caracter especial utilizar pyperclip.copy
pa.hotkey('ctrl', 'v')
time.sleep(1)
pa.press('tab')

texto = f'''Prezado, boa tarde.

Segue relatório do orçamento, referente ao ano de 2023.

Qualquer dúvida estou à disposição.
Atenciosamente.'''

pyperclip.copy(texto)
pa.hotkey('ctrl', 'v')
time.sleep(2)
pa.click(x=964, y=702)
time.sleep(1)
pa.click(x=382, y=641)
pasta = f'D:\Power Bi\Dados\Excel'
pyperclip.copy(pasta)
time.sleep(1)
pa.press('enter')
time.sleep(2)
pa.click(x=359, y=420)
time.sleep(1)
pyperclip.copy('Planilha de Orçamento')
time.sleep(1)
pa.hotkey('ctrl', "v")
pa.press('enter')
time.sleep(3)
pa.click(x=837, y=702)
print('Seu e-mail foi enviado com sucesso.')


