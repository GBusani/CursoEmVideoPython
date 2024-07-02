from random import shuffle

a1 = input('Digite o primeiro nome: ')
a2 = input('Digite o segundo nome: ')
a3 = input('Digite o terceiro nome: ')
a4 = input('Digite o quarto nome: ')
os = [a1, a2, a3, a4]

shuffle(os)

print('A ordem sorteada foi\n{}'.format(os))
