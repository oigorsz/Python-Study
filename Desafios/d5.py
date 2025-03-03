# Crie um programa que utilize um laço for para percorrer os números de 1 a 100 e calcule a soma dos números ímpares.

soma = 0
lista = []

for i in range (1, 101):
    if i%2 != 0:
        lista.append(i)
        soma += i

print(soma)

for i in range (len(lista)):
    if i < len(lista) - 1:
        print(lista[i], end = ', ')
    else:
        print(lista[i])
