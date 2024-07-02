frase = str(input('Digite uma frase: ')).strip().lower().split()
frase = ''.join(frase)

i = 0
k = len(frase)
for c in range(0, k):
    if frase[c] != frase[k - 1 - c]:
        i += 1
if i == 0:
    print('A frase é um PALÍNDROMO!')
else:
    print('A frase NÃO é um palíndromo.')
