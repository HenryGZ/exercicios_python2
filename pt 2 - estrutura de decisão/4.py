letra = str(input('informe uma letra: ')).upper().strip()[0]

if letra in 'AEIOU':
    print('vogal')
else:
    print('consoante')