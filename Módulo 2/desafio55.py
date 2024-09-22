maior = 0
menor = 0

for n in range (1, 6):
    peso = float(input('Digite o peso da {}* pessoa: '.format(n)))

    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso foi de {:.2f}Kg.'.format(maior))
print('O menor peso foi de {:.2f}Kg'.format(menor))

    