termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
i = 1
while i != 11:
    print('Termo {:2}: {}'.format(i, termo1))
    termo1 += razao
    i += 1
