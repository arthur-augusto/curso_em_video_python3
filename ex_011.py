# Calcula o quantos litros de tinta é necessário para pintar uma parede
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
litros = area / 2
print(f'Sua parede tem a dimensão de {largura} x {altura} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisará de {litros}l de tinta.')
