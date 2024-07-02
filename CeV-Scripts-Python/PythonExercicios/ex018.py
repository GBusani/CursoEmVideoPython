import math

a = float(input('Digite o valor de um ângulo: '))
x = math.radians(a)

print('O ângulo {:.1f} tem seno {:.2f}, cosseno {:.2f}, e tangente {:.2f}'.format(a, math.sin(x), math.cos(x), math.tan(x)))
