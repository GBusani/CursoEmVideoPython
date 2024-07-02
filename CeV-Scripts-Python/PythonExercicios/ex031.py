dist = int(input('Digite uma distância em Km: '))

if dist <= 200:
    print('O preço é R${:.2f}'.format(dist * 0.5))
else:
    print('O preço é R${:.2f}'.format(dist * 0.45))
