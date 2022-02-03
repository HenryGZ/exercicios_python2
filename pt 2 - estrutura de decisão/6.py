n1 = int(input('informe o primeiro número: '))
n2 = int(input('informe o segundo número: '))
n3 = int(input('informe o terceiro número: '))

if(n1 > n2):
    maior = n1
else:
    maior = n2
if (maior < n3):
    maior = n3

print(f'o maior número é {maior}')