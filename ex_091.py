# Mostra os valores sorteados para 4 jogadores e o ranking entre eles
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
cont = 1
print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'{k} tirou o {v} no dado.')
    sleep(1)
print('-=' * 30)
ranking = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))
print(f'{"== RANKING DOS JOGADORES ==":^30}')
for k, v in ranking.items():
    print(f'  {cont}º lugar: {k} com {v}.')
    cont += 1
    sleep(1)
