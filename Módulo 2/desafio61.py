a0 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
n = a0
i = 1

while  i <= 10:
    print('{} - {}.'.format(i, n))
    n += r
    i += 1



