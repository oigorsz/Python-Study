n = int(input('Digite um número inteiro: '))
fatorial = 1

i = n

while i >= 1:
    fatorial *= i
    i += -1

print('O fatorial de {} é {}.'.format(n, fatorial))
