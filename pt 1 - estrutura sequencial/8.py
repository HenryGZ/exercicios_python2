def salario(horas, ganho):
    return horas * ganho

ganho = (float(input('informe quanto ganha por hora: ')))
horas = (int(input('informe quantas horas trabalha por mês: ')))
print(f'seu salário mensal é de: {salario(horas, ganho)}')