num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3


if(num1 == num2== num3):
    print('Todos os números são iguais.')
else:
    print('{} é o maior número.'.format(maior))
    print('{} é o menor número.'.format(menor))


