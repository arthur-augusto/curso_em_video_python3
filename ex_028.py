# O algoritmo sorteia um número aleatório entre 0 e 5 e o usuário tenta adivinhar
from random import randint
from time import sleep
print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)
palpite_computador = randint(0, 5)
palpite_usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if palpite_usuario == palpite_computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {palpite_computador} e não no {palpite_usuario}')
