# Calcula a soma de todos os números multiplos de 3 entre 1 e 500
soma = 0
n_valores = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n_valores += 1
        soma += c
print(f'A soma dos {n_valores} valores é de solicitados é {soma}')
