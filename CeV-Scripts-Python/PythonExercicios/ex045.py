from random import choice

player = str(input('Pedra, Papel, Tesoura!\n')).strip().capitalize()

computador = choice(['Pedra', 'Papel', 'Tesoura'])

print('Computador: {}\nJogador: {}'.format(computador, player))
if player == computador:
    print('Empate! Tente novamente!')
elif player == 'Pedra' and computador == 'Tesoura' or player == 'Papel' and computador == 'Pedra' or player == 'Tesoura' and computador == 'Papel':
    print('Parabéns! Você ganhou!')
elif player == 'Papel' and computador == 'Tesoura' or player == 'Tesoura' and computador == 'Pedra' or player == 'Pedra' and computador == 'Papel':
    print('O computador ganhou!')
else:
    print('Jogada Inválida! Digite uma das 3 opções:\n[Pedra]\n[Papel]\n[Tesoura]')
