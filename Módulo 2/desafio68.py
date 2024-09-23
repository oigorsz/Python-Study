import random

vitorias = 0
numero_jogador = -1
numero_maquina = -1
lado_jogador = ''
lado_maquina = ''

print('JOGO ÍMPAR OU PAR.\n')

while True:

    while not(lado_jogador == 'P' or lado_jogador == 'I'):
        lado_jogador = str(input('Escolha ímpar ou par(I/P): ')).upper()

        if(lado_jogador == 'P'):
            lado_maquina == 'I'
        else:
            lado_maquina = 'P'

    while not(0 <= numero_jogador and numero_jogador <= 10):
        numero_jogador = int(input('Escolha um número de 1 até 10: '))
        numero_maquina = random.randint(1, 10)

    soma = numero_maquina + numero_jogador

    print(f'JOGADOR : {numero_jogador}.')
    print(f'MAQUINA: {numero_maquina}.')
    print(f'SOMA: {soma}')

    if (soma %2 == 0 and lado_jogador == 'P') or (soma % 2 != 0 and lado_jogador == 'I'):
        print('JOGADOR GANHOU !')
        vitorias += 1
        numero_jogador = -1 #RESETA O NÚMERO DO JOGADOR
        numero_maquina = -1
        lado_jogador = ''
        lado_maquina = ''

    else:
        print('VOCÊ PERDEU.')
        break

print('RESULTADOS: ')
print(f'VITÓRIAS: {vitorias}.')

        

        
