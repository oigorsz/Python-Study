nome = str(input('Digite o seu nome completo: '))
nome = nome.capitalize()


dividir = nome.split()
Pnome = dividir[0]
Fnome = dividir[-1]


print('nome completo : {}'.format(nome))
print('primeiro nome  : {}'.format(Pnome.capitalize()))
print('último nome : {}'.format(Fnome.capitalize()))