num_pessoas_mais18 = 0
num_homens = 0
num_mulheres_menos20 = 0
total = 0

print('CADASTRO DE PESSOAS: ')

while True:
    sexo = ''
    idade = 0
    op = ''

    while not(op == 'S' or op == 'N'):
        op = str(input('Deseja cadastrar mais ? (S/N)')).upper()

    if(op == 'S'):
        #CADASTRAR
        while not(idade > 0 and idade < 150):
            idade = int(input('Digite a idade: '))
        
        while not(sexo == 'M' or sexo == 'F'):
            sexo = str(input('Digite o sexo (M/F): ')).upper()

        if idade >= 18:
            num_pessoas_mais18 += 1
        if sexo == 'M':
            num_homens += 1
        if idade < 20 and sexo == 'F':
            num_mulheres_menos20 += 1


        total += 1
    else:
        print('FIM DOS CADASTROS.')
        break


print('ANÁLISE GERAL: ')
print(f'TOTAL DE CADASTROS: {total}')
print(f'PESSOAS MAIORES DE 18 ANOS: {num_pessoas_mais18}')
print(f'NÚMERO DE HOMENS: {num_homens}')
print(f'NÚMERO DE MULHERES MENORES QUE 20 ANOS: {num_mulheres_menos20}')