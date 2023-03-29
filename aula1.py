import pyautogui
import mouse
import keyboard 
import time
# Acessar o google e pesquisar sobre a copa do mundo 2022

# Obter a posição do mouse através do Eixo X e Y
""" while  True:
   print(mouse.get_position())
   time.sleep(1) """
# Comando para pressionar a tecla windows no teclado  'win'
# pyautogui.write -> escrever algum texto que estiver entre aspas
# pyautogui.hotkey -> pressionar teclas que são atalho para abrir uma nova guia no Google chrome  
# mouse.move -> move o mouse para as coordenadas indicadas no pixel da tela, através do eixo X e Y
# pyautogui.click -> clica nas coordenas indicadas no pixel da tela através do eixo X e Y, também pode ser utilizado com imagens.
# time.sleep -> Utilizado para determinar um intervalo de tempo, para executar a próxima ação no código.
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.hotkey ("ctrl", "t") 
mouse.move(1499, 86, 3)
pyautogui.click(1499, 86, 1)
pyautogui.write("www.google.com")
mouse.move(1848, 305, 3)
mouse.click('left')
time.sleep(3)
keyboard.write('Copa libertadores 2023')
keyboard.press('enter')
time.sleep(5)




