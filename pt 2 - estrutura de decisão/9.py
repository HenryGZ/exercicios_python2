turno = str(input('informe o turno que voce estuda: ')).strip().upper()[0]

if turno in 'M':
    print('bom dia!')
elif turno in 'V':
    print('boa tarde!')
else:
    print('boa noite!')