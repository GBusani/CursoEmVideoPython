l = float(input('Digite a largura em metros: '))
h = float(input('Digite a altura em metros: '))

a = l * h
t = a / 2

print('A área da parede é de {} metros quadrados e precisa de {:.1f} litros de tinta'.format(a, t))
