# Jogo ímpar ou par com o computador
from random import randint
print('=' * 30)
print('   VAMOS JOGAR ÍMPAR OU PAR')
print('=' * 30)
n_vitorias = 0
tipo = ' '
while True:
    numero_jogador = int(input('Digite um valor: '))
    while tipo not in 'PI':
        opcao_jogador = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    numero_computador = randint(1, 10)
    soma = numero_jogador + numero_computador
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'
    print('-' * 30)
    print(f'Você jogou {numero_jogador} e o computador {numero_computador}. Total de {soma} DEU {resultado}')
    print('-' * 30)
    if resultado[0] == opcao_jogador:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        n_vitorias += 1
    else:
        print('Você PERDEU!')
        break
print('=' * 30)
print(f'GAME OVER! Você venceu {n_vitorias} vezes.')
