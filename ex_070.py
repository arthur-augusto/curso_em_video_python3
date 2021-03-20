# Calcula o total de quantos produtos o usuário desejar e mostra estatísticas sobre eles
print('-' * 34)
print('        LOJA SUPER BARATÃO')
n_produtos = total = n_caros = meno = 0
nome_barato = ''
while True:
    print('-' * 34)
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    n_produtos += 1
    total += preco
    if preco > 1000:
        n_caros += 1
    if n_produtos == 1 or preco < menor:
        menor = preco
        nome_barato = nome
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''--------- FIM DO PROGRAMA --------
O total da compra foi R${total:.2f}
Temos {n_caros} produtos custando mais de R$1000.00
O produto mais barato foi {nome_barato} que custa R${menor:.2f}''')
