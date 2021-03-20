# Mostra os 10 primeiros termos de uma PA
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(1, 11):
    print(termo, end=' -> ')
    termo += razao
print('ACABOU')
