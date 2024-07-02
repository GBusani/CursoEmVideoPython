termo1 = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
i = 1
total = 11
adcional = 0
while i != total:
    print('Termo {:2}: {}'.format(i, termo1))
    termo1 += razao
    i += 1
    if i == total:
        adcional = int(input('Deseja mais quantos termos? '))
        total += adcional
