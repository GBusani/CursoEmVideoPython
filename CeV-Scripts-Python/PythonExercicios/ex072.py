a = ('zero','um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
     'dez', 'onze', 'doze', 'treze', 'quatorze', 
    'quinze', 'dezesseis', 'dezessete', 'dezoito',
    'dezenove', 'vinte')
num = int(input('Digite um número de 0 a 20: '))
while num < 0 or num > 20:
    num = int(input('TENTE NOVAMENTE. Digite um número de 0 a 20: '))
print(f'Você digitou o número {a[num]}.')
