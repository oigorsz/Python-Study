n = int(input('Digite um número inteiro: '))
div = 0

for i in range (n, 0, -1):
    if(n % i == 0):
        div += 1
    
    if(div > 2):
        break

if(div <= 2):
    print('{} é primo.'.format(n))
else:
    print('{} não é primo.'.format(n))