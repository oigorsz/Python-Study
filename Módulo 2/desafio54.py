from datetime import datetime

ano_atual = datetime.now().year
maiores = 0
menores = 0

for n in range (0, 7, 1):
    ano_nascimento = int(input('Digite o ano de nascimento da {}* pessoa: '.format(n + 1)))

    if (ano_atual - ano_nascimento >= 18):
        maiores += 1
    else:
        menores += 1

print('{} pessoas são maiores de idades.'.format(maiores))
print('{} pessoas são menores de idade.'.format(menores))