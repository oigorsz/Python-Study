a0 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
n = a0

for i in range (1, 11, 1):
    print('{} - {}.'.format(i, n))
    n += r
