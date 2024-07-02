from random import randint
i = 0
num = -1
computador = randint(0,10)
while num != computador:
    num = int(input('Digite um número de 0 a 10: '))
    i += 1
    if num == computador:
        print('Parabéns! Você adivinhou na {}ª tentativa! O número que eu pensei foi {}'.format(i, computador))
    else:
        print('Tente novamente! {}ª tentativa.'.format(i))
