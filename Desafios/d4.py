#Crie um programa que solicite ao usuário um número inteiro 
# e use um laço for para verificar se esse número é primo. 
# Um número é primo quando é maior que 1 e não tem divisores além de 1 e ele mesmo.

while True :
    n = int(input("Digite um número inteiro positivo: "))

    if n <= 0:
        print('Digite um valor válido.')
    else:
        break

if n == 1:
    print(f'{n} não é um número primo')
else: 
    for i in range (2, n ):
        if n % i == 0:
            print(f'{n} não é um número primo')
            break
    else:
        print(f'{n}  é um número primo')

        


