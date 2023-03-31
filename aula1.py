# Acessar o google e pesquisar sobre a copa do mundo 2022

# Obter a posição do mouse através do Eixo X e Y
""" while  True:
   print(mouse.get_position())
   time.sleep(1) """
# Comando para pressionar a tecla windows no teclado  'win'
# pyautogui.write -> escrever algum texto que estiver entre aspas
# pyautogui.position
# pyautogui.hotkey -> pressionar teclas que são atalho para abrir uma nova guia no Google chrome  
# mouse.move -> move o mouse para as coordenadas indicadas no pixel da tela, através do eixo X e Y
# pyautogui.click -> clica nas coordenas indicadas no pixel da tela através do eixo X e Y, também pode ser utilizado com imagens.
# time.sleep -> Utilizado para determinar um intervalo de tempo, para executar a próxima ação no código.

import pyautogui
import mouse
import keyboard 
import time
import pyperclip
import pandas as pd
import os

'''pesquisa = input('Digite o assunto a ser pesquisado: ')


time.sleep(2)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")
pyautogui.hotkey ("ctrl", "t") 
mouse.move(1499, 86, 3)
pyautogui.click(1499, 86, 1)
pyautogui.write("www.google.com")
pyautogui.press('enter')
mouse.move(1848, 305, 3)
mouse.click('left')
time.sleep(2)
keyboard.write(pesquisa)
keyboard.press('enter')
time.sleep(2)
'''

#print(pyautogui.position())
os.chdir('C:\Users\AlanCarvalhodeSouza\OneDrive - KEEGGO TECHNOLOGY BRASIL S A\Documentos\Intensivão de Python\Aula 1')
tabela = pd.read_excel('Vendas - Dez.xlsx')
print(tabela)

