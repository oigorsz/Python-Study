ano = int(input('Digite um ano: '))

if ano % 4 == 0 or ano % 400 == 0:
    print('Ano Bissexto')
else:
    print('Ano não é Bissexto')