maior = 0
menor = 1000
for c in range(0, 5):
    peso = float(input('Digite seu peso: '))
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso
print('Maior peso: {}\nMenor peso: {}'.format(maior, menor))
