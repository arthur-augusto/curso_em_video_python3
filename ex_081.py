# Mostra cadastro sobre os valores digitados
numeros = []
while True:
    numero = int(input('Digite um valor: '))
    numeros.append(numero)
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
if 5 in numeros:
    cinco = 'faz'
else:
    cinco = 'não faz'
numeros.sort(reverse=True)
print('-=' * 30)
print(f'''Você digitou {len(valores)} elementos.
Os valores na ordem decrescente são {numeros}
O valor 5 {cinco} parte da lista!''')
