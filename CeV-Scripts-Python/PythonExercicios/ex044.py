valor = float(input('Digite o preço R$[00.00]: '))
forma = int(input('''Para pagar à vista no dinheiro/cheque, digite [1]
Para pagar à vista no cartão, digite [2]
Para pagar em até 2x no cartão, digite [3]
para pagar em 3x ou mais no cartão, digite [4]\n'''))

if forma == 1:
    print('Preço final R${:.2f}'.format(valor * 0.9))
elif forma == 2:
    print('Preço final R${:.2f}'.format(valor * 0.95))
elif forma == 3:
    print('Preço final R${:.2f}'.format(valor))
else:
    print('Preço final R${:.2f}'.format(valor * 1.05))
