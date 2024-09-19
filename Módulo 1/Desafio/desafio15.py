quilometros = float(input('Quantos quilometros foram rodados: '))
dias = int(input('Quantos dias o carro ficou alugado: '))

preco = 60*dias +0.15*quilometros

print('O Carro foi alugado por {} dias e rodou {:.2f}Km.'.format(dias, quilometros))
print("Custo da diária: R${:.2f}".format(dias * 60))
print("Custo da quilometragem: R${:.2f}".format(quilometros * 0.15))
print('O valor final ficou em R${:.2f}.'.format(preco))
