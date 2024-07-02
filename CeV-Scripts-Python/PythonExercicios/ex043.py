peso = float(input('Digite seu peso em Kg (utilize "." caso necessário): '))
altura = float(input('Digite sua altura em metros (utilize "." caso necessário): '))

IMC = peso / altura**2

if IMC < 18.5:
    print('[{:.1f}]:\nAbaixo do peso ideal'.format(IMC))
elif IMC < 25:
    print('[{:.1f}]:\nPeso ideal'.format(IMC))
elif IMC < 30:
    print('[{:.1f}]:\nSobrepeso'.format(IMC))
elif IMC < 40:
    print('[{:.1f}]:\nObesidade'.format(IMC))
else:
    print('[{:.1f}]:\nObesidade mórbida'.format(IMC))
