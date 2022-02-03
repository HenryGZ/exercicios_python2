
from time import sleep
import os

#verifica se o arquivo existe, se não existir ele cria o arquivo
def verifica():
    arquivo = r"C:\Users\henry\OneDrive\Documentos\Python\exercícios python 3\pt 2 - estrutura de decisão\suspeitos.txt"
    os.path.exists(arquivo)
    if os.path.exists(arquivo) == False:
        arquivo = open('suspeitos.txt', 'a')

#função de escrita no arquivo txt
def armazenamento(resultado, nome):
    arquivo = open('suspeitos.txt', 'a')
    arquivo.write('\n______________________\n')
    arquivo.write(nome +'\n')
    arquivo.write(resultado)
    arquivo.close()

#função que faz a contagem e o julgamento, retorna o resultado
def contagem(tel, loc, mora, trab):
    i = 0
    decisao = 'indefinido'
    if tel in 'S':
        i += 1
    if loc in 'S':
        i += 1
    if mora in 'S':
        i += 1
    if trab in 'S':
        i += 1
    if (i <= 1):
        decisao = 'Inocente'
    elif (i == 2):
        decisao = 'Suspeito'
    elif (i == 3):
        decisao = 'Cumplice'
    elif (i == 4 ):
        decisao = 'Assasino'
    return decisao

#função principal que faz o cadastro
print('_______________report de crime_______________')
nome = str(input('informe o nome do suspeito: '))
tel = str(input('telefonou para a vítima? [S/N]')).strip().upper()[0]
loc = str(input('esteve no local?  [S/N]')).strip().upper()[0]
mora = str(input('mora perto da vítima?  [S/N]')).strip().upper()[0]
trab = str(input('já trabalhou com a vítima?  [S/N]')).strip().upper()[0]
print('_____________________________________________')
print('calculando resultado....')

resultado = contagem(tel, loc, mora, trab)
verifica()
armazenamento(resultado, nome)

sleep(0.5)
print(f'Decisão: {resultado}')
