#Crie um programa Python que identifique todos os números entre 
# 100 e 300 (inclusive) que são divisíveis por 7, mas não múltiplos de 5. 
# Os números identificados devem ser exibidos em uma única linha, separados por vírgulas.

import numpy as np

vetor = np.array([])

for i in range (100, 301, 1):
    if i%7 == 0 and i%5 != 0:
        vetor = np.append(vetor, i)


print(", ".join(map(str, vetor.astype(int))))