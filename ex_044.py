# Calcula o novo preço de um produto com base na forma de pagamento
print('=' * 10, end='')
print(' LOJAS PÍTON ', end='')
print('=' * 10)
preco_inicial = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    preco_final = preco_inicial - (preco_inicial * 10 / 100)
elif opcao == 2:
    preco_final = preco_inicial - (preco_inicial * 5 / 100)
elif opcao == 3:
    preco_final = preco_inicial
    valor_parcelas = preco_final / 2
    print(f'Sua compra será parcelada em 2x de R${valor_parcelas:.2f} SEM JUROS')
elif opcao == 4:
    n_parcelas = int(input('Quantas parcelas? '))
    preco_final = preco_inicial + (preco_inicial * 20 / 100)
    valor_parcelas = preco_final / n_parcelas
    print(f'Sua compra será parcelada em {n_parcelas}x de R${valor_parcelas:.2f} COM JUROS')
else:
    preco_final = preco_inicial
    print('Opção Inválida! Tente novamente.')
print(f'Sua compra de R${preco_inicial:.2f} vai custar R${preco_final:.2f} no final.')
