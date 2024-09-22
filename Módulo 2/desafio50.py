#Solicitar 6 números e realizar a soma apenas dos números pares
soma = 0

for i in range (0, 6, 1):
    n = int(input('Digite um número {}: '.format(i + 1)))
    #Se o número for par, somar
    if(n % 2 == 0):
        print('{} SOMADO.'.format(n))
        soma += n
    else:
        print('{} NÃO SOMADO.'.format(n))

print('SOMA DOS PARES: {}.'.format(soma))