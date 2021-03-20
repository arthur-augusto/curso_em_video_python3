# Verifica se é possivel aprovar um empréstimo baseado no valor da casa, salário e o tempo de financiamento
valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (anos * 12)
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')
if prestacao <= salario_comprador * (30 / 100):
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
