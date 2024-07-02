nome = str(input('Digite seu nome completo: ')).strip()

maiuscula = nome.upper()

minuscula = nome.lower()

tudo = len(nome)
espaco = nome.count(' ')
caracteres = tudo - espaco

lista = nome.split()
nome1 = len(lista[0])

print('Nome: {} \n em maiúscula: {} \n em minúscula: {}'.format(nome, maiuscula, minuscula))
print(' possui {} letras \n possui {} letras no primeiro nome'.format(caracteres, nome1))
