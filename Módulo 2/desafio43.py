massa = float(input('Digite a massa corpórea, em Kg: '))
altura = float(input('Digite sua altura, em metros: '))

imc = massa/(altura *altura)

print('O SEU IMC É DE : {:.2f}.'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc < 25:
    print('Peso ideal.')
elif imc < 30:
    print('Sobrepeso.')
elif imc < 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')