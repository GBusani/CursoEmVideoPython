n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

if media < 5:
    print('Aluno \033[1;31mREPROVADO\033[m com {:.1f} pontos'.format(media))
elif media >= 5 and media < 7:
    print('Aluno \033[1;36mEM RECUPERAÇÃO\033[m com {:.1f} pontos'.format(media))
else:
    print('Aluno \033[1;32mAPROVADO\033[m com {:.1f} pontos'.format(media))
