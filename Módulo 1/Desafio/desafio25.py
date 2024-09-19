nome = str(input('Digite o seu nome completo: '))

print('O nome {}'.format(nome))

if nome.upper().find('SILVA') != -1 :
    print('possui SILVA')
else :
    print('não possui SILVA')