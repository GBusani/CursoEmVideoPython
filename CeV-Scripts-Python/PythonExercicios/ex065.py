i = n = soma = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    i += 1
    soma = soma + n
    if i == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
media = soma / i
print('''A média dos valores é {}
O MAIOR valor é {}
O MENOR valor é {}'''.format(media, maior, menor))
