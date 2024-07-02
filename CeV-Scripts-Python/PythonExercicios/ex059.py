count = 0
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
while count != 5:
    count = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Qual é a sua opção? '''))
    if count == 1:
        print('A soma de {} e {} é igual a {}'.format(num1, num2, num1 + num2))
    elif count == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(num1, num2, num1 * num2))
    elif count == 3:
        if num1 > num2:    
            print('{} é MAIOR que {}'.format(num1, num2))
        elif num2 > num1:
            print('{} é MAIOR que {}'.format(num2, num1))
        else:
            print('{} é IGUAL a {}'.format(num1))
    elif count == 4:
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
