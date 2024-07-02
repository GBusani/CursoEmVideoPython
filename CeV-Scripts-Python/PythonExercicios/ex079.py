ListaNums = []
resposta = 'S'

while resposta == 'S':
    Num = (int(input('Digite um número inteiro: ')))
    if Num in ListaNums:
        print('Valor duplicado. Número não adcionado.')
    else:
        ListaNums.append(Num)
        print('Número adcionado com sucesso.')
        resposta = input('Deseja continuar? [S/N]\n').strip().upper()[0]
    while not (resposta == 'S' or resposta == 'N'):
        resposta = input('Deseja continuar? [S/N]\n').strip().upper()[0]
print('-='*30)
print(f'Você digitou os valores {sorted(ListaNums)}')
