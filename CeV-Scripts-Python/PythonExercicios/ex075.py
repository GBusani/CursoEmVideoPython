from itertools import count
i = 0
num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))

print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu, pela 1ª vez, no {num.index(3) + 1}º lugar')
else:
    print('O número 3 não foi digitado')
print('Os números pares digitados foram: ', end = '')
for n in num:
    if n % 2 == 0:
        print(n, end = ' ')
