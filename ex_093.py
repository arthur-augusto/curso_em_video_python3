# Mostra cadastro de partidas de um jogador
jogador = dict()
lista_gols = list()
jogador['nome'] = str(input('Nome do Jogador: ')).strip()
n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for p in range(1, n_partidas + 1):
    lista_gols.append(int(input(f'    Quantos gols na {p}ª partida? ')))
jogador['gols'] = lista_gols[:]
jogador['total'] = sum(lista_gols)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {n_partidas} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'  => Na {i + 1}ª partida, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
