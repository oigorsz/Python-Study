# Informe os n primeiros números da sequência de fibonacci - método sem recursão

n = int(input("Informe a quantidade de número da sequência de fibonacci: "))
x0 = 1
x1 = 1

if n <= 0 :
    print('Valor Inválido.')

elif n == 1:
    print(f'{x0}', end = ' ')
else:
    print(f'{x0}', end = ' ')
    print(f'{x1}', end = ' ')

    for i in range (3, n + 1):
        x2 = x1 + x0
        print(f'{x2}', end = ' ')
        x0 = x1
        x1 = x2
