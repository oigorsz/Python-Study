n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))

if(n1 == n2):
    print('{} e {} são iguais.'.format(n1,n2))
elif (n1 > n2):
    print('{} é maior que {}.'.format(n1, n2))
else:
    print('{} é menor que {}.'.format(n1, n2))