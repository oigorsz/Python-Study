#Calculadora de empréstimo

print('Bem vindo ao calculadora de empréstimo !\n')
nome = str(input('Qual o seu nome ? '))

casa = float(input('{}, qual o valor da casa que deseja comprar, em reais: '.format(nome)))
salario = float(input(('{}, qual o seu salário atual, em reais: '.format(nome))))
tempo = int(input(('{}, em quantos anos deseja pagar a casa: '.format(nome))))

parcelaMensal = casa/(tempo * 12)

if parcelaMensal <= 0.3*salario:
    print('O EMPRÉSTIMO FOI APROVADO !')
    print('VALOR DA CASA: R${:.2f}.'.format(casa))
    print('VALOR DA PARCELA: R${:.2f}.'.format(parcelaMensal))
    print('QUANTIDADE DE MÊSES: {}.'.format(tempo * 12))
else :
    print('O EMPRÉSTIMO NÃO FOI APROVADO !')
    print('O valor da prestação mensal excedeu em 30% do seu salário')
    print('VALOR DO SALÁRIO: R${:.2f}.'.format(salario))
    print('VALOR DA PARCELA: R${:.2f}'.format(parcelaMensal))
