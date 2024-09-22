frase = str(input('Digite uma frase: '))
palavra = frase.upper().split()
junto = ''.join(palavra)
inverso = ''


for i in range(len(junto) - 1, -1, - 1):
    inverso += junto[i]

print('ORIGINAL: {}\nINVERSO: {}'.format(junto, inverso))

if(inverso == junto):
    print('PALÍNDROMO')
else:
    print('NÃO É PALÍNDROMO')