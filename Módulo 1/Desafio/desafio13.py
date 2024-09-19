preco = float(input('Qual o preço do produto ? '))
print('O produto custa R${:.2f} e sai a R%{:.2f} com 5% de desconto'.format(preco, preco*0.95))