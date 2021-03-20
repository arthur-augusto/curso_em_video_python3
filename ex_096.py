# Mostra a área de um terreno a partir de uma função
def area_terreno(medida1, medida2):  # Imprime a medida da área
    area = medida1 * medida2
    print(f'A área de um terreno retangular de {medida1} x {medida2} é de {area}m².')


print('Controle de Terrenos')
print('-' * 20)
lar = float(input('LARGURA (m): '))
com = float(input('COMPRIMENTO (m): '))
area_terreno(lar, com)
