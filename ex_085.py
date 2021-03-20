# Mostra uma lista com os valores pares digitados e outra com os ímpares
valores = [[], []]
for v in range(1, 8):
    valor = int(input(f'Digite o {v}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print('-=' * 30)
print(f'''Os valores pares digitados foram: {valores[0]}
Os valores impares digitados foram: {valores[1]}''')
