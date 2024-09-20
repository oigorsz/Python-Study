preco = float(input('Digite o valor total da compra, em reais: '))

print('FORMAS DE PAGAMENTO.\n')
print('[1] À VISTA DINHEIRO/CHEQUE.')
print('[2] À VISTA NO CARTÃO.')
print('[3] 2x NO CARTÃO CRÉDITO.')
print('[4] 3x OU MAIS NO CARTÃO CRÉDITO.')

op = int(input('Qual a sua opção: '))

if op == 1:
    desconto = preco * 0.1
    print('VALOR FINAL: R${:.2f}.'.format(preco - desconto))
    print('VALOR DO DESCONTO: R${:.2f}.'.format(desconto))
elif op == 2:
    desconto = preco * 0.05
    print('VALOR FINAL: R${:.2f}.'.format(preco - desconto))
    print('VALOR DO DESCONTO: R${:.2f}.'.format(desconto))
elif op == 3:
    print('SUA COMPRA SERÁ PARCELADA EM 2x DE R${:.2f}.'.format(preco / 2))
    print('VALOR FINAL: R${:.2f}.'.format(preco))
elif op == 4:
    parcelas = int(input('Número de parcelas: '))
    valor_final = preco * 1.2  # Aplicar 20% de acréscimo
    valor_parcela = valor_final / parcelas
    print('SUA COMPRA SERÁ PARCELADA EM {}x DE R${:.2f}.'.format(parcelas, valor_parcela))
    print('VALOR FINAL: R${:.2f}.'.format(valor_final))
else:
    print('Digite uma opção válida.')
