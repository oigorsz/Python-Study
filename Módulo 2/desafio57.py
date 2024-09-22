sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo de uma pessoa: ')).upper()
    if (sexo != 'M' and sexo != 'F'):
        print('DIGITE UM VALOR VÁLIDO !')

if sexo == 'M':
    print('MASCULINO')
else:
    print('FEMININO')