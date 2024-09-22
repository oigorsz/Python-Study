soma = 0
lidos = 0
n = 0

while n != 999:
    print('CONDIÇÃO DE PARADA: N = 999')
    n = int(input('Digite um número inteiro: '))

    if n != 999:
        soma += n
        lidos += 1
    else:
        print('FIM DA CONTAGEM !\n')

print('SOMA DOS NÚMEROS: {}.'.format(soma))
print('NÚMEROS LIDOS: {}.'.format(lidos))