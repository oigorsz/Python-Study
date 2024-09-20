ano = int(input('Digite o ano de nascimento: '))
idade = 2024 - ano

print('idade: ',idade)
if(idade == 18):
    print('HORA DE SE ALISTAR !')
elif (idade < 18):
    print('AINDA NÃO É NECESSÁRIO SE ALISTAR.')
    print('TEMPO DE RETORNO:')

    if(18 - idade == 1):
        print('{} ANO.'.format(18 - idade))
    else:
        print('{} ANOS.'.format(18 - idade))

else:
    print('JÁ DEVERIA TER SIDO ALISTADO.\n')
    print('TEMPO DE ATRASO: ')
    if(idade - 18== 1):
        print('{} ANO.'.format(idade - 18))
    else:
        print('{} ANOS.'.format(idade - 18))