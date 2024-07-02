vel = int(input('Digite uma velocidade em Km/h: '))

if vel <= 80:
    print('Joinha -b')
else:
    print('Você foi multado em R${},00'.format((vel - 80) * 7))
