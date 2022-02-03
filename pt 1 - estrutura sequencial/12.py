lata = galao = 0
area = float(input('informe a área a ser pintada: '))
while (area - 18 >= 0 ):
    area = area - 18
    lata += 1
while (area - 3.6 >= 0 ):
    area = area - 3.6
    galao += 1

galao += 1 #um pouco a mais para nao faltar

print(f'serão necessários {lata} latas de 18L e {galao} galões de 3,6L.')
print(f'total a ser pago é de: {(lata * 80) + (galao * 25)} reais.')

