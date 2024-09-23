soma = 0
produots_maisde1000 = 0
nome_produto_mais_barato = ''
valor_produto_mais_barato = 0
numero_produtos = 0

print('MERCADO BAUMBAUM.\n')
while True:
    op = ''

    while not(op == 'S' or op == 'N'):
        op = str(input('Deseja adicionar produto? (S/N)')).upper()

    if(op == 'S'):
        #CADASTRAR
        nome = str(input('Digite o nome do produto: '))
        valor = float(input('Digite o preço do produto, em reais: '))

        print('\nADICIONADO: ')
        print(f'PRODUTO - {nome}')
        print(f'PREÇO: R${valor:.2f}.\n')

        #Determinar o produto mais barato
        if(numero_produtos == 0):
            nome_produto_mais_barato = nome
            valor_produto_mais_barato = valor
        else:
            if valor < valor_produto_mais_barato:
                nome_produto_mais_barato = nome
                valor_produto_mais_barato = valor

        numero_produtos += 1

        #Número de produtos que custam mais de R$1000
        if(valor > 1000):
            produots_maisde1000 += 1

        #Soma dos produtos adicionados
        soma += valor
    else:
        print('FINALIZANDO COMPRAS.')
        break

print(f'TOTAL DA COMPRA: R${soma:.2f}')
print(f'PRODUTO MAIS BARATO: R${valor_produto_mais_barato:.2f} - {nome_produto_mais_barato}')
print(f'NÚMERO DE PRODUTOS ACIMA DE R$1000: {produots_maisde1000}')