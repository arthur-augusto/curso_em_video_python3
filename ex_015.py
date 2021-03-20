# Calcula o preço do aluguel de um carro
dias = int(input('Quantos dias alugados? '))
quilometros = float(input('Quantos Km rodados? '))
total = (60 * dias) + (quilometros * 0.15)
print(f'O total a pagar é de R${total:.2f}')
