from random import randint
i = 0
print('''Vamos jogar Par ou Ímpar! Vamos ver quantas vezes seguidas você consegue ganhar!
[1] PAR
[2] ÍMPAR''')
while True:
    computador = randint(0,5)
    par_impar = int(input('Par ou Ímpar: '))
    jogador = int(input('Digite um número: '))
    if par_impar == 1:
        if (jogador + computador) % 2 == 0:
            i += 1
            print(f'''{jogador} + {computador} = {jogador + computador} -> PAR
VITÓRIA! Você venceu pela {i}ª vez!''')
        else:
            print(f'''{jogador} + {computador} = {jogador + computador} -> ÍMPAR
DERROTA. Você venceu um total de {i} vezes!''')
            break
    elif par_impar == 2:
        if (jogador + computador) % 2 == 1:
            i += 1
            print(f'''{jogador} + {computador} = {jogador + computador} -> ÍMPAR
VITÓRIA! Você venceu pela {i}ª vez!''')
        else:
            print(f'''{jogador} + {computador} = {jogador + computador} -> PAR
DERROTA. Você venceu um total de {i} vezes!''')
            break
    else:
        print('''ERRO! Tente novamente, digitando [1/2] para PAR ou ÍMPAR, respectivamente.
Para o número, digite qualquer valor inteiro não negativo (0 ou maior).''')
        break
