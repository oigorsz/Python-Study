distancia = float(input('Digite a distância da viagem em Km: '))
custo = 0
taxa = 0

if distancia <= 200:
    print('Distância até 200Km o preço por Km é de R$0.50.\n')
    taxa = 0.5
    
else :
    print('Distância maior que 200Km o preço por Km é de R$0.45.\n')
    taxa = 0.45

custo = distancia * taxa
print('CUSTO TOTAL: R${:.2f}.'.format(custo))
print('CUSTO POR Km: R${:.2f}.'.format(taxa))
