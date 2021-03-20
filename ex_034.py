# Calcula o aumento de 15% ou 10% baseado no salário informado pelo usuário
salario = float(input('Qual é o salário do funcionário? R$'))
salario_aumentado = salario + (salario * 15 / 100)
if salario > 1250:
    salario_aumentado = salario + (salario * 10 / 100)
print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_aumentado:.2f} agora.')
