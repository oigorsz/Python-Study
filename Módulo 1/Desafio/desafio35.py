c1 = float(input('Digite o primeiro comprimento, em metros: '))
c2 = float(input('Digite o segundo comprimento, em metros: '))
c3 = float(input('Digite o terceiro comprimento, em metros: '))


if (c2 + c3 > c1) and (c1 + c3 > c2) and (c1 + c2 > c3):
    print('As retas formam um triângulo.\n')
else:
    print('As retas não foram um triângulo.\n')


