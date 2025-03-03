#Objetivo: Criar um programa que imprima a tabuada de multiplicação de um número fornecido pelo usuário, 
# mas somente para múltiplos que sejam maiores que 50.

n = int(input("Informe um número inteiro: "))

if n > 50:
    for i in range (1, 11):
        print(f'{n} x {i} = {n * i}')
else:
    print('Informe um número maior que 50')