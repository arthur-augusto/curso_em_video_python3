# Calcula o fatorial de um número
fatorial = 1
numero = int(input('Digite um número para calcular o seu fatorial: '))
print(f'Calculando {numero}! = ', end='')
for ant in range(numero, 0, -1):
    if ant == 1:
        print(f'{ant} = ', end='')
    else:
        print(f'{ant} x ', end='')
    fatorial *= ant
print(fatorial)
