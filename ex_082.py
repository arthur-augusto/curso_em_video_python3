# Mostra a lista dos números digitados pelo usuário, uma lista com os pares e outra com os ímpares
numeros = []
pares = []
impares = []
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print(f'''A lista completa é {numeros}
A lista de números pares é {pares}
A lista de números ímpares é {impares}''')
