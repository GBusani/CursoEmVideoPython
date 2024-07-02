SumIdade = 0
NomeM = 'None'
idadeM = 0
i = 0

for c in range(0, 4):
    print('FICHÁRIO {}:'.format(c + 1))
    nome = str(input('Nome:\n')).strip()
    idade = int(input('Idade:\n'))
    sexo = str(input('Sexo: [M/F]\n')).strip().capitalize()
    SumIdade = SumIdade + idade
    if sexo == 'M' and idade > idadeM:
            NomeM = nome
    elif sexo == 'F' and idade < 20:
          i += 1
MediaIdade = SumIdade / 4
print('''Média de idade: {:.1f}
Nome do homem mais velho: {}
Mulheres com menos de 20 anos: {}'''.format(MediaIdade, NomeM, i))
