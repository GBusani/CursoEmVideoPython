num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 >= num2 and num1 >= num3:
    if num2 <= num3:
        print('Maior: {}\nMenor: {}'.format(num1, num2))
    else:
        print('Maior: {}\nMenor: {}'.format(num1, num3))
elif num2 >= num3 and num2 >= num1:
    if num1 <= num3:
        print('Maior: {}\nMenor: {}'.format(num2, num1))
    else:
        print('Maior: {}\nMenor: {}'.format(num2, num3))
else:
    if num1 <= num2:
        print('Maior: {}\nMenor: {}'.format(num3, num1))
    else:
        print('Maior: {}\nMenor: {}'.format(num3, num2))
