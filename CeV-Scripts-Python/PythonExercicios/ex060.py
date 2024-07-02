num = int(input('Digite um número inteiro positivo para calcular seu fatorial: '))
fatorial = num
i = 1
while num != i:
    fatorial = fatorial * (num - i)
    i = i + 1
print('O fatorial de {} é igual a {}'.format(num, fatorial))
