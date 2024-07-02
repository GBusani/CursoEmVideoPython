from datetime import date
atual = date.today().year

i = 0
j = 0

for c in range(0, 7):
    data = int(input('Digite seu ano de nascimento: '))
    ano = atual - data
    if ano < 18:
        i += 1
    else:
        j += 1
print('{} pessoas não atingiram a maioridade, e {} já tem maioridade.'.format(i, j))
