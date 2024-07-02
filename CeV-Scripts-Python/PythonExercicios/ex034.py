sal = float(input('Digite seu salário: '))

if sal > 1250:
    print('Seu novo salário é R${:.2f}'.format(sal * 1.1))
else:
    print('Seu salário é R${:.2f}'.format(sal * 1.15))
