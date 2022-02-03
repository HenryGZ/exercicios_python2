import time

dia = int(input('informe o número do dia da semana: '))

if(dia == 1):
    print(f'dia {1} é domingo')
elif(dia == 2):
    print(f'dia {2} é segunda')
elif(dia == 3):
    print(f'dia {3} é terça')
elif(dia == 4):
    print(f'dia {4} é quarta')
elif(dia == 5):
    print(f'dia {5} é quinta')
elif(dia == 6):
    print(f'dia {6} é sexta')
elif(dia == 7):
    print(f'dia {7} é sabado')
else:
    print('a semana não possui esse dia')

time.sleep(2)

import pyautogui

pyautogui.position()
pyautogui.moveTo(1339, 767)
time.sleep(0.5)
pyautogui.leftClick()