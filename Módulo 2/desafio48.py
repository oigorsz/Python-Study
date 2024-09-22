#Soma de todos os números multiplos de 3 que são ímpares que estão no intervalo de 1 até 500

soma = 0


for n in range (3, 500, 3):
    if n % 2 != 0:
        soma += n




print('SOMA: {}'.format(soma))