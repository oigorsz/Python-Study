n = int(input('Digite um número inteiro: '))

print('TABUADA DO {}.'.format(n))

for i in range (0, 11, 1):
    print('{} X {} = {}'.format(i, n, n * i))

print('FIM')