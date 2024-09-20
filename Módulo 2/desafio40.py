nota1 = float(input('Digite a nota da prova 1: '))
nota2 = float(input('Digite a nota da prova 2: '))

media = (nota1 + nota2)/2

print('NOTA FINAL : {:.2f}.'.format(media))

if media < 5:
    print('REPROVADO.')
elif 5 <= media and media < 7:
    print('RECUPERAÇÃO')
else :
    print('APROVADO !')
