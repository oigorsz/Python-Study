#Crie um programa que utilize um laço for para imprimir todos os números pares entre 1 e 20.

#Utilizando o for
lista = []

for i in range(1, 21, 1):
    if i%2 == 0:
        lista.append(i)


for i in range(len(lista)):
    if i < len(lista) - 1 :
        print(lista[i], end = ', ')
    else:
        print(lista[i])

#Utilizando o while
lista2 = []

i = 1
while i <= 20 :
    if i % 2 != 0:
        lista2.append(i)
    i = i + 1

for i in range (len(lista2)):
    if i < len(lista2) - 1:
        print(lista2[i], end= ', ')
    else:
        print(lista2[i])



