# Analisa o peso de várias pessoas
pessoas = []
pessoa = []
maior = menor = 0
while True:
    nome = str(input('Nome: ')).strip()
    peso = float(input('Peso: '))
    if len(pessoas) == 0:
        maior = menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa[:])
    pessoa.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print(f'''Ao todo, você cadastrou {len(pessoas)} pessoas.
O maior peso foi de {maior}Kg. Peso de ''', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
