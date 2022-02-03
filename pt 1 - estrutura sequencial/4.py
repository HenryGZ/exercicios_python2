notas = []

def media(notas):
    soma = 0
    for c in range(len(notas)):
        soma += notas[c]
    return soma / 4
    
for i in range(4):
    notas.append(float(input(f'informe a nota numero {i+1}: ')))


print(f'a média foi de {media(notas)}')