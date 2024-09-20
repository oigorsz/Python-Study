import random
numero = random.randrange(1, 5, 1)
escolha = int(input('Digite um número de 1 a 5: '))

print('Você escolheu {} e a máquina escolheu {}.\n'.format(escolha, numero))

if escolha == numero:
    print('Você acertou !')
else:
    print('Você errou !')

print('FIM')


