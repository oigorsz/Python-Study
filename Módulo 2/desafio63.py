n = int(input('Digite o número de elementos: '))
i = n
ant = 0
atual = 1

while i >= 0:
    print('{}'.format(ant))
    proximo = atual + ant
    ant = atual
    atual = proximo
    i = i - 1
   

    
