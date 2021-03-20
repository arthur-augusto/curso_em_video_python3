# Calcula o preço de uma viagem de x quilometros
distancia = float(input('Qual é a distancia da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print(f'Você está prestes a inciar uma viagem de {distancia}Km')
print(f'E o preço da sua passagem será de R${preco:.2f}')
