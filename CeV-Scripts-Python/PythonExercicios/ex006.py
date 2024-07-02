n = int(input('Digite um número: '))

print('\033[45mO dobro é {}\033[m,\033[46m o triplo é {}\033[m,\033[41m e a raiz quadrada é {:.3f}\033[m'.format(n * 2, n * 3, n**(1/2)))
