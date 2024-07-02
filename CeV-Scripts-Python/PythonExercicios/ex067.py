num = i = 1
print('Cálculo da tabuada. Digite qualquer número negativo para parar.')
while True:
    if i == 1:
        print('-=-' * 10)
        num = int(input('Digite um valor: '))
    if num < 0:
        break
    print(f'{num} x {i:2} = {num * i}')
    i += 1
    if i == 11:
        i = 1
print('Programa tabuada ENCERRADO.')
