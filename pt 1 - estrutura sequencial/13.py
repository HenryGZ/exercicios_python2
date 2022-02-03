def tempo(velocidade, tamanho):
    return tamanho/velocidade

velocidade = float(input('informe a velocidade da sua conexão em MB/s: '))
tamanho = float(input('informe em MB o tamanho do arquivo: '))
print(f'o dowload irá demorar {tempo(velocidade, tamanho)} segundos')
print(f'ou aproximadamente {round(tempo(velocidade, tamanho) / 60)} minutos')