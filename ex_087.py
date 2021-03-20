# Mostra cadastro sobre uma matriz com valores informados pelo usuário
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_3linha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            soma_3linha += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for e in matriz[l]:
        print(f'[{e:^5}]', end='')
    print('')
print('-=' * 30)
print(f'''A soma dos valores pares é {soma_pares}.
A soma dos valores da terceira coluna é {soma_3linha}.
O maior valor da segunda linha é {max(matriz[1])}.''')
