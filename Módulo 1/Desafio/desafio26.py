nome = str(input('Digite o seu nome: '))

numA = nome.upper().count('A')
PosAI = nome.upper().find('A')
PosAF = nome.upper().rfind('A')

print('O nome {} possui {} letras "A", a primeira aparece na posição {} e a última na posiçõa {}'.format(nome, numA,PosAI,PosAF))