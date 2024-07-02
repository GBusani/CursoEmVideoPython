from random import randint

computador = randint(0,5)

num = int(input('Digite um número de 0 a 5: '))

if num == computador:
    print('Venceu!')
else:
    print('Perdeu! Eu pensei no número {} e não no {}'.format(computador, num))
