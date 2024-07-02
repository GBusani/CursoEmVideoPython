
maioridade = homens = mulheres_20 = int(0)
while True:
    idade = int(0)
    sexo = continuar = ''
    print('-' * 30)
    while idade <= 0:
        idade = int(input('Idade: '))
    while not (sexo == 'M' or sexo == 'F') :
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres_20 += 1
    while not (continuar == 's' or continuar == 'n') :
        continuar = str(input('Deseja continuar? [s/n] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'''{maioridade} pessoas tem mais de 18 anos.
{homens} homens.
{mulheres_20} mulheres com menos de 20 anos.''')
