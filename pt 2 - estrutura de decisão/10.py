sal = float(input('informe seu salário:'))

if (sal <= 280):
    novosal = sal * 1.20
    aumento = 20
elif(sal < 700):
    novosal = sal * 1.15
    aumento = 15
elif(sal < 1500):
    novosal = sal * 1.10
    aumento = 10
elif(sal >= 1500):
    novosal = sal * 1.05
    aumento = 5
print('______________________________________________')
print(f'o novo salário é de: R$ {novosal}')
print(f'o percentual de aumento foi de: {aumento}%')
print(f'o valor aumentado foi de: R$ {novosal - sal}')
print('______________________________________________')