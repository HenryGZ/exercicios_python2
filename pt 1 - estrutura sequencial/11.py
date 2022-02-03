h = int(input('informe sua altura em cm: '))
sx = str(input('informe seu sexo (M/F): ')).strip().upper()[0]

if sx in 'M':
    print ((72.7*h) - 58)
elif sx in 'F':
    print ((62.1*h) - 44.7)
else:
    print('sexo inválido!!')

