i = soma = caro = 0
nome_barato = ''
while True:
    preco = int(0)
    continuar = nome = ''
    print('=' * 30)
    while nome == '':
        nome = str(input('Nome do produto: ')).strip()
    while preco <= 0:
        preco = float(input('Preço: R$'))
    i += 1
    soma += preco
    if preco > 1000:
        caro += 1
    if i == 1:
        preco_barato = preco
        nome_barato = nome
    elif preco < preco_barato:
        preco_barato = preco
        nome_barato = nome
    while not (continuar == 's' or continuar == 'n'):
        continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'''O valor total foi R${soma:.2f}
{caro} produtos custam mais de R$1000.00
O produto mais barato é {nome_barato}, que custa R${preco_barato:.2f}''')
