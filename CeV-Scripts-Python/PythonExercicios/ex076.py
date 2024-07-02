precos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
          'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
          'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

for cont in range(0, len(precos)):
    if cont % 2 == 0:
        print(f'{precos[cont]:.<30}', end = ': ')
    else:
        print(f'R${precos[cont]:>7.2f}')