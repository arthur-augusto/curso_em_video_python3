# Baseado na quantidade de dinheiro que o usuário quer sacar informar quantos tipos de nota pode sacar
print('=' * 25)
print('       BANCO PÍTON')
print('=' * 25)
n_notas50 = n_notas20 = n_notas10 = n_notas1 = 0
valor = int(input('Que valor você quer sacar? R$'))
if valor >= 50: # Verifica se é preciso usar notas de 50
    while valor >= 50: # Verifica quantas notas de 50 são necessárias
        valor -= 50
        n_notas50 += 1
if valor >= 20:
    while valor >= 20:
        valor -= 20
        n_notas20 += 1
if valor >= 10:
    while valor >= 10:
        valor -= 10
        n_notas10 += 1
if valor >= 1:
    while valor >= 1:
        valor -= 1
        n_notas1 += 1
if n_notas50 > 0:
    print(f'Total de {n_notas50} notas de R$50')
if n_notas20 > 0:
    print(f'Total de {n_notas20} notas de R$20')
if n_notas10 > 0:
    print(f'Total de {n_notas10} notas de R$10')
if n_notas1 > 0:
    print(f'Total de {n_notas1} notas de R$1')
print('=' * 25)
print('Volte sempre ao BANCO PÍTON! Tenha um bom dia!')
