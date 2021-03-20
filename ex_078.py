# Mostra os maiores e menores valores dos 5 que o usuário digitou
valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {v}: ')))
print('-=' * 30)
print(f'''Você digitou os valores {valores}
O maior valor digitado foi {max(valores)} nas posições ''', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for i, v in enumerate(valores):
    if v == min(valores):
        print(f'{i}... ', end='')
