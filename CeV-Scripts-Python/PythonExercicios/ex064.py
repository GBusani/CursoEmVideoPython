i = n = soma = 0
while n != 999:
     n = int(input('Digite um número. Para parar, digite [999]: '))
     if n != 999:
          i += 1
          soma = soma + n
print('A soma dos {} números, foi {}'.format(i, soma))
