# Mostra quantos termos da sequência de fibonacci que o usuário desejar
print('-' * 26)
print('  Sequência de Fibonacci')
print('-' * 26)
t1 = 0
t2 = 1
t3 = 1
n_termos = int(input('Quantos termos você quer mostrar? '))
for t in range(1, n_termos + 1):
    print(f'{t1} -> ', end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
print('FIM')
