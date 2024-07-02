num = int(input('Digite um número: '))
i = 0

for c in range(1, num):
    if num % c == 0:
        i += 1
if i == 1:
    print('O número {} é primo!'.format(num))
else:
    print('O número {} NÃO é primo.'.format(num))
