# Mostra os divisores de um número e se ele é primo ou não
numero = int(input('Digite um número: '))
n_divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        n_divisores += 1
        print(f'{c}*', end=' ')
    else:
        print(c, end=' ')
print(f'\nO número {numero} foi divisível {n_divisores} vezes.')
if n_divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
