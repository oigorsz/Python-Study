import random

maquina = random.randint(0, 10)  # máquina escolhe um número entre 1 e 10, incluindo os extremos
jogador = -1  # inicializar jogada
jogadas = 0

while jogador != maquina:
    jogador = int(input('Digite um número de 0 até 10: '))
    jogadas += 1

    if jogador < 0 or jogador > 10:
        print('Número inválido! Digite um número entre 0 e 10.')
    elif jogador < maquina:
        print('VOCÊ ERROU, TENTE UM NÚMERO MAIOR.')
    elif jogador > maquina:
        print('VOCÊ ERROU, TENTE UM NÚMERO MENOR.')

print('\nVOCE CONSEGUIU !')
print('MAQUINA : {}.'.format(maquina))
print('VOCÊ TENTOU {} VEZES.'.format(jogadas))
