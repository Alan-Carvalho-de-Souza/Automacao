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
time.sleep(3)
pa.write('gmail.com')
pa.press('enter')
time.sleep(2)
pa.click(x=75, y=207)
