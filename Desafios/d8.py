# Informe os n primeiros números da sequência de fibonacci - método sem recursão


def fibonacci (n):
    if n <= 1 :
        return n
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)


n = int(input("Informe a quantidade de número da sequência de fibonacci: "))
x0 = 1
x1 = 1

for i in range (1, n + 1):
    print(fibonacci(i), end=' ')


    
