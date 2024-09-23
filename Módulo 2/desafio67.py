while True:
    n = int(input('ESCOLHA UM NÚMERO NATURAL: '))

    if(n < 0):
        print('FIM DO PROGRAMA.')
        break

    print(f'TABUADA DO {n}.\n')

    for i in range(1, 11):
        print(f'{n} X {i} = {n * i}')
    
    print('\n')