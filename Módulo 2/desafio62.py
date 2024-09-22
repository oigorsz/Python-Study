a0 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão da PA: '))
n = a0
i = 1
numTermos = 1


while  i <= 10:
    print('{} - {}.'.format(i, n))
    n += r
    i += 1

pf = i

while numTermos > 0:
    print('Quantos termos você deseja mostrar a mais ?')
    numTermos = int(input('Digite aqui: '))

    if numTermos > 0:
        while i < numTermos + pf:
            print('{} - {}.'.format(i, n))
            n += r
            i += 1

        pf = i

    
        


    

