casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o seu salário mensal: '))
anos = int(input('Digite quantos anos pretende pagar: '))

parcela = (casa / 12) / anos

print('A parcela a pagar é R${:.2f} por {} meses'.format(parcela, anos * 12))
if parcela / sal > 0.3:
    print('Infelizmente, seu salário é insuficiente para o financiamento')
else:
    print('Emprétimo concedido')
