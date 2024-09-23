num_contados = 0
soma = 0

while True:
    n = int(input('Digite um número: '))

    if(n == 999):
        print('FIM DE RECEBIMENTO.\n')
        break
    else:
        print(f'{n} RECEBIDO.')

    num_contados += 1
    soma += n

print(f'A SOMA É {soma}.')
print(f'A QUANTIDADE DE NÚMEROS INSERIDOS É {num_contados}.')



