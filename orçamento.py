"""
Testando conhecimentos de automação de tarefas

Objetivo criar uma automação, para enviar uma planilha com os dados de orçamento pessoal via e-mail
"""

import pandas as pd
import pyautogui as pa
import time
import pyperclip

#time.sleep(4)
#print(pa.position())

pa.click(x=556, y=748)
time.sleep(2)
pa.write('gmail.com')
pa.press('enter')
time.sleep(2)
pa.click(x=75, y=207)
time.sleep(2)
pa.write('alan_carvalho_96@hotmail.com')
pa.press('tab')
time.sleep(2)
pa.press('tab')
time.sleep(2)
pyperclip.copy('Teste de automação') # Quando houver caracter especial utilizar pyperclip.copy
pa.hotkey('ctrl', 'v')
time.sleep(1)
pa.press('tab')

texto = f'''Prezado, boa tarde.

Segue relatório do orçamento, referente ao ano de 2023.

Qualquer dúvida estou à disposição.
Atenciosamente.'''

pyperclip.copy(texto)
pa.hotkey('ctrl', 'v')

