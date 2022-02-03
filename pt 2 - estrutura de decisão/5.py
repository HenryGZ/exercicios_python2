n1 = float(input('informe a nota do 1º trimestre: '))
n2 = float(input('informe a nota do 2º trimestre: '))
n3 = float(input('informe a nota do 3º trimestre: '))

media = (n1 + n2 + n3)/3

if(media >= 60):
    print(f'aprovado, média: {media}')
elif(media < 60):
    print(f'reproado, média: {media}')
elif(media == 100):
    print(f'aprovado com excelencia, média: {media}')