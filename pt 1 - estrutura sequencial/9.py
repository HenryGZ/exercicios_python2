def conversor(tmp):
    return 5 * ((tmp-32) / 9)

tmp = float(input('informe a temperatura em fahrenheit: '))
print(f'a temperatura em celsius é de {conversor(tmp)}')