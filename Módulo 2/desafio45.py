import random

print('JOGO DO JOKEPO')
print('ESCOLHA UMA OPÇÃO: ')
print('1 - PEDRA\n2 - PAPEL\n3 - TESOURA ')

robo = random.randint(1, 3)

op = int(input('ESCOLHA UMA OPÇÃO ACIMA: '))

if op == 1:
    op = 'PEDRA'
elif op == 2:
    op = 'PAPEL'
else:
    op = 'TESOURA'

if robo == 1:
    robo = 'PEDRA'
elif robo == 2:
    robo = 'PAPEL'
else:
    robo = 'TESOURA'


print('ESCOLHAS:\nJOGADOR 1: {}.\nMÁQUINA :{}.'.format(op, robo))

if(op == robo):
    print('EMPATE')
elif (op == 'PEDRA'):
    if(robo == 'PAPEL'):
        print('VOCê PERDEU')
    else:
        print('VOCÊ GANHOU')

elif (op == 'PAPEL'):
    if(robo == 'TESOURA'):
        print('VOCê PERDEU')
    else:
        print('VOCÊ GANHOU')

elif (op == 'TESOURA'):
    if(robo == 'PAPEL'):
        print('VOCê PERDEU')
    else:
        print('VOCÊ GANHOU')
