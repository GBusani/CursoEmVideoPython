from datetime import date
atual = date.today().year

ano = int(input('Qual seu ano de nascimento?\n'))

idade = atual - ano

if idade < 18:
    print('Faltam {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você deve se alistar neste ano.')
else:
    print('Faz {} anos que seu alistamento já passou.'.format(idade - 18))
