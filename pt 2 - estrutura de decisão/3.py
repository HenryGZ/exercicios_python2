sx = str(input('informe o sexo [F/M]: ')).upper().strip()[0]

if sx in 'F':
    print('feminino')
elif sx in 'M':
    print('masculino')
else:
    print('sexo inválido')