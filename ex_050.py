# Mostra a dos pares entre os 6 numeros informados pelo usuário
soma = 0
cont_par = 0
for c in range(1, 7): # Pede para o usuário digitar um número 6 vezes
    numero = int(input('Digite o {}° número: '.format(c)))
    if numero % 2 == 0: # Verifica se o número digitado pelo usuário é par
        soma += numero
        cont_par += 1
print(f'A soma entre os {cont_par} números pares digitados é {soma}')
