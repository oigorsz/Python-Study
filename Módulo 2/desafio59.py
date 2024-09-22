n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
op = 0

while op != 5:
    print('\n[1] SOMAR\n[2] SUBTRAIR\n[3] MULTIPLICAR\n[4] DIVIDIR\n[5] SAIR DO PROGRAMA')
    op = int(input('Escolha uma opção: '))

    if op == 1:
        print('A SOMA de {:.2f} com {:.2f} é {:.2f}.\n'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('A SUBTRAÇÃO de {:.2f} com {:.2f} é {:.2f}.\n'.format(n1, n2, n1 - n2))
    elif op == 3:
        print('A MULTIPLICAÇÃO de {:.2f} com {:.2f} é {:.2f}.\n'.format(n1, n2, n1 * n2))
    elif op == 4:
        if n2 != 0:
            print('A DIVISÃO de {:.2f} por {:.2f} é {:.2f}.\n'.format(n1, n2, n1 / n2))
        else:
            print('Erro! Não é possível dividir por zero.\n')
    elif op == 5:
        print('PROGRAMA ENCERRADO.\n')
    else:
        print('Digite uma opção válida.\n')
