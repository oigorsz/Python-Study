salario = float(input('Digite o seu salário, em reias: '))
taxa = 0

if salario > 1250:
    taxa = 0.1
else:
    taxa = 0.15

print('SALÁRIO ATUAL: R${:.2f}.'.format(salario))
print('SALÁRIO NOVO: R${:.2f}.'.format(salario *(1 + taxa)))
print('AUMENTO PERCENTUAL: {:.2f}%.'.format(taxa*100))
