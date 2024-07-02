saque = 0
while saque <= 0:
    saque = int(input('Qual o valor a ser sacado? R$'))
while True:
    if saque >= 50:
        cinquenta = saque // 50
        saque = saque % 50
        print(f'Total de {cinquenta} cédulas de R$50')
    if saque >= 20:
        vinte = saque // 20
        saque %= 20
        print(f'Total de {vinte} cédulas de R$20')
    if saque >= 10:
        dez = saque // 10
        saque %= 10
        print(f'Total de {dez} cédulas de R$10')
    if saque != 0:
        print(f'Total de {saque} cédulas de R$1')
        break
    else:
        break
