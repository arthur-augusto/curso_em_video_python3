# Sorteia quantos jogos da mega sena o usuário desejar
from random import randint
from time import sleep
jogo = []
print('-' * 40)
print(f'{"PALPITES MEGA SENA":^40}')
print('-' * 40)
n_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'---------- SORTEANDO {n_jogos:>2} JOGOS ----------')
for j in range(1, n_jogos + 1):
    contador = 0
    while True:
        numero = randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            contador += 1
        if contador == 6:
            break
    jogo.sort()
    print(f'Jogo {j:>2}: {jogo}')
    jogo.clear()
    sleep(1)
print(f'{" < BOA SORTE! > ":-^40}')
