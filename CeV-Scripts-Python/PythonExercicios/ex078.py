vals = list() 

for i in range(0,5):
    vals.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = vals[i]
        menor = vals[i]
    elif maior < vals[i]:
        maior = vals[i]
    elif menor > vals[i]:
        menor = vals[i]    
print('=-' * 30)
print(f'Você digitou os valores {vals}')

print(f'O maior valor digitado foi {maior} na posição', end=' ')
for i, v in enumerate(vals):
    if vals[i] == maior:
        print(f'{i};', end = ' ')
print()
print(f'O menor valor digitado foi {menor} na posição', end=' ')
for i, v in enumerate(vals):
    if vals[i] == menor:
        print(f'{i};', end = ' ')
print()
