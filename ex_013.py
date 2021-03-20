# Calcula o reajuste salarial de 15% de aumento
salario_inicial = float(input('Qual é o salario do funcionário? R$'))
salario_final = salario_inicial + (salario_inicial * 15 / 100)
print(f'Um funcionário que ganhava R${salario_inicial:.2f}, com 15% de aumento, passa a receber R${salario_final:.2f}')
