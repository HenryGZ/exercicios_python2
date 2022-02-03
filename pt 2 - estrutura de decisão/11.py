hr = int(input('informe as horas trabalhadas: '))
val = float(input('informe o valor da hora: '))
sal = hr * val

if(900< sal <= 1500):
    ir = 0.05
elif(sal <=2500):
    ir = 0.10
elif(sal > 2500):
    ir = 0.20

print('______________________________________')
print(f'salário bruto: R${sal}')
print(f'Imposto de Renda (IR): R${sal * ir}')
print(f'INSS: R${sal * 0.10}')
print(f'FGTS recolhido: R${sal * 0.11}')
print(f'total de descontos: R${(sal * ir)+(sal * 0.10)}')
print('______________________________________')
print(f'salário liquido: R${sal - ((sal * ir)+(sal * 0.10))}')


