import math

co = float(input('Digite o comprimento do cateto oposto, em metros: '))
ca = float(input('Digite o comprimento do cateto adjacente, em metros: '))

h = math.hypot(co, ca)

print('A hipotenusa é {:.2f}m'.format(h))