brasileirao2024 = ('Flamengo', 'Bahia', 'Botafogo', 'São Paulo',
                   'Athletico-PR', 'Bragantino', 'Palmeiras', 'Internacional',
                   'Cruzeiro', 'Atlético-MG', 'Fortaleza', 'Grêmio',
                   'Vasco da Gama', 'Juventude', 'Fluminense', 'Criciúma',
                   'Corinthians', 'Atlético-GO', 'EC Vitória', 'Cuiabá')
i = 0

print('\nTOP 5\n')
while i < 5:
    print(f'{i + 1}º - {brasileirao2024[i]}')
    i += 1
i = -3

print('\nÚLTIMOS 4\n')
while i < 1:
    print(f'{20 + i}º - {brasileirao2024[i]}')
    i += 1

OrdAlf = sorted(brasileirao2024)
x = ', '.join(OrdAlf)
print(f'\nORDEM ALFABÉTICA\n{x}')

if 'Chapecoense' in brasileirao2024:
    print(f'\nChapecoense está em {brasileirao2024.index("Chapecoense") + 1}º lugar\n')
else:
    print('\nChapecoense não está no TOP 20.\n')
