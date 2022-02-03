import os

def verifica(): 
    ler = r"C:\Users\henry\OneDrive\Documentos\Python\exercícios python 3\pt 2 - estrutura de decisão\suspeitos.txt"
    os.path.exists(ler)
    if os.path.exists(ler) == False:
        print('o arquivo informado não exite.')

verifica()
arquivo = open('suspeitos.txt')
linhas = arquivo.readlines()
for i in linhas:
    print(i)





