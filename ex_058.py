# Sorteia um número entre 0 e 10 e o usuário deve adivinhar
from random import randint
print('''Sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
tentativas = 1
computador = randint(0, 10)
palpite = int(input('\nQual é seu palpite? '))
while palpite != computador:
    if palpite < computador:
        print('\nMais... Tente mais uma vez.')
    else:
        print('\nMenos... Tente mais uma vez.')
    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
