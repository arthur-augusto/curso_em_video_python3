# Calcula os 10 primeiros termos de uma PA e mais quantos o usuário desejar
print('-=' * 10)
c_termos = 0
n_termos = 10
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
while n_termos != 0:
    for t in range(1, n_termos + 1):
        print(f'{termo} -> ', end='')
        termo += razao
        c_termos += 1
    print('PAUSA')
    n_termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progresão finalizada com {c_termos} termos mostrados.')
