# Verifica a velocidade de um carro e caso esteja acima do limite irá mostrar o valor da multa
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    valor_multa = (velocidade - 80) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    print(f'Você deve pagar uma multa de R${valor_multa}!')
print('Tenha um bom dia! Dirija com segurança!')
