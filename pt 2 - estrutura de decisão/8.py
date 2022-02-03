n1 = int(input('informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('informe o terceiro número: '))

if(n1 > n2):
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if (maior < n3):
    maior = n3

if(maior == n1 or maior == n2 and menor == n1 or menor == n2):
    meio = n3
if(maior == n1 or maior == n3 and menor == n1 or menor == n3):
    meio = n2
else:
    meio = n1

print(f'o maior número é {maior} o do meio é {meio} e o menor é {menor}')
