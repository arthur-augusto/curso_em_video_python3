# Mostra cadastro sobre 4 valores informados pelo usuário
valores = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição.')
else:
    print('O valor não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
