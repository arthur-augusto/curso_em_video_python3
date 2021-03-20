# Mostra uma lista de preços
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
itens = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2,
        'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
for i in itens:
    if itens.index(i) % 2 == 0:
        print(f'{i:.<31}', end='')
    else:
        print(f'R${i:>7.2f}')
print('-' * 40)
