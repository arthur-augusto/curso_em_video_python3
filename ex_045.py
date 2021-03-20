# Joga pedra, papel ou tesoura com o usuário
from random import randint
from time import sleep
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcoes = ['Pedra', 'Papel', 'Tesoura']
jogada_usuario = int(input('Qual é a sua jogada? '))
jogada_computador = randint(0, 2) # Computador escolhe entre as 3 opções
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 12)
print(f'''Computador jogou {opcoes[jogada_computador]}
Jogador jogou {opcoes[jogada_usuario]}''')
print('-=' * 12)
if jogada_usuario == 0: # Jogador jogou PEDRA
    if jogada_computador == 0: # Computador jogou PEDRA
        print('EMPATE')
    elif jogada_computador == 1: # Computador jogou PAPEL
        print('JOGADOR PERDE')
    else:                       # Computador jogou TESOURA
        print('JOGADOR VENCE')
elif jogada_usuario == 1: # Jogador jogou PAPEL
    if jogada_computador == 0: # Computador jogou PEDRA
        print('JOGADOR VENCE')
    elif jogada_computador == 1: # Computador jogou PAPEL
        print('EMPATE')
    else:                       # Computador jogou TESOURA
        print('JOGADOR PERDE')
elif jogada_usuario == 2: # Jogador jogou TESOURA
    if jogada_computador == 0: # Computador jogou PEDRA
        print('JOGADOR PERDE')
    elif jogada_computador == 1: # Computador jogou PAPEL
        print('JOGADOR VENCE')
    else:                       # Computador jogou TESOURA
        print('EMPATE')
else: # Jogador escolheu uma OPÇÃO INVÁLIDA
    print('OPÇÃO INVÁLIDA! Tente novamente.')
