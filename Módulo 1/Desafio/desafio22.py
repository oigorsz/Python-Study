nome = str(input('Digite o seu nome: '))
dividirNome = nome.split()


print('Nome Maiúsculo: {}'.format(nome.upper()))
print('Nome Minúsculo: {}'.format(nome.lower()))
print('Número de letras: {}'.format(len(nome) - nome.count(' ')))
print('Número de letras do primeiro nome: {}'.format(len(dividirNome[0])))