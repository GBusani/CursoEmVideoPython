print('Cálculo dos 10 primeiros termos de uma PA')
termo1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for c in range(0,10):
    print('Termo {:2}: {}'.format(c + 1, termo1))
    termo1 += r
