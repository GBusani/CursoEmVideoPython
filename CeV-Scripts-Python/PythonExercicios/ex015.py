km = float(input('Digite a quantidade de kilometros percorridos: '))
d = int(input('Digite quantos dias o carro foi alugado: '))

c = (d * 60) + (km * 0.15)

print('O preço a pagar é {:.2f} reais'.format(c))