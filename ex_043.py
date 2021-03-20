# Calcula o IMC baseado na massa e na altura e indica a sua faixa de peso
massa = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = massa / altura ** 2
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO DO PESO ideal.')
elif imc <= 25:
    print('PARABÉNS, você está na faixa de PESO IDEAL!')
elif imc <= 30:
    print('Você está em SOBREPESO.')
elif imc <= 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
