num = int(input('Escolha um número para mostrar sua tabuada: '))

print('-' * 12)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 12)
