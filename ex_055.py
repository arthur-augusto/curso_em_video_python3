# Mostra o maior e o menor peso informado pelo usuário entre 5 pessoas
maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa: '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'''O maior peso lido foi de {maior:.1f}Kg
O menor peso lido foi de {menor:.1f}Kg''')
