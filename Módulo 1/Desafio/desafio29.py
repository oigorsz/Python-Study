velocidade = float(input('Digite a velocidade atual do carro em Km/h: '))
multa = 0

if velocidade > 80 :
    print('Você ultrapassou o limite de velocidade em {}Km !'.format(velocidade - 80))
    multa = (velocidade - 80)*7
    print('MULTADO: R${:.2f}.'.format(multa))
else:
    print('Continue dirigindo com segurança e responsabilidade !')
