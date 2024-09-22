soma_idades = 0
homem_mais_velho = 'Nenhum'
idade_mais_velha_homem = -1
num_mulheres_menorq20 = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa (M/F): '.format(i))).strip().upper()

    soma_idades += idade

    if sexo == 'M':
        if idade > idade_mais_velha_homem:
            idade_mais_velha_homem = idade
            homem_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            num_mulheres_menorq20 += 1

media_idades = soma_idades / 4
print('Média de idade: {:.2f}'.format(media_idades))

if homem_mais_velho == 'Nenhum':
    print('Não existe nenhum homem.')
else:
    print('O homem mais velho é {} e possui {} anos.'.format(homem_mais_velho, idade_mais_velha_homem))

print('{} mulheres têm menos de 20 anos.'.format(num_mulheres_menorq20))
