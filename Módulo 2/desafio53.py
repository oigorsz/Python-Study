# Entrada da frase
frase = input('Digite uma frase: ').replace(" ", "").lower()  # Remove espaços e converte para minúsculas
p = 0  # Indicador de palíndromo

# Verifica se a frase é um palíndromo
for i in range(0, len(frase) // 2):  # Comparar apenas até a metade
    if frase[i] != frase[-(i + 1)]:  # Compara caractere da frente com o de trás
        p = 1
        break  # Se encontrar diferença, pode parar

if p == 1:
    print('{} não é palíndromo.'.format(frase))
else:
    print('{} é palíndromo.'.format(frase))
