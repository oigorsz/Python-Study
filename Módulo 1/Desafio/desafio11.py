altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))
area = altura * largura
tinta = area/2

print('Um muro com {:.2f}m de altura e {:.2f}m de largura possui {:.2f}m2'.format(altura, largura, area))
print('Para pintar esse muro serão necessários {:.2f}litros de tinta'.format(tinta))
