# Mostra os cadastro das partidas de vários jogadores
jogadores = list()
jogador = dict()
lista_gols = list()
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).strip()
    n_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, n_partidas + 1):
        lista_gols.append(int(input(f'    Quantos gols na {p}ª partida? ')))
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)
    jogadores.append(jogador.copy())
    lista_gols.clear()
    jogador.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if opcao == 'N':
        break
print('-=' * 30)
print(f'{"cod":<4}{"nome":<15}{"gols":<21}{"total":>5}')
print('-' * 45)
for i, j in enumerate(jogadores):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<21}{j["total"]:>5}')
print('-' * 45)
while True:
    cod = int(input('Mostrar cadastro de qual jogador? (999 para parar) '))
    if cod not in range(0, len(jogadores)) and cod != 999:
        print(f'ERRO! Não existe jogador com o código {cod}!')
    elif cod == 999:
        break
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
        for jogo, gol in enumerate(jogadores[cod]['gols']):
            print(f'    No {jogo + 1}º jogo fez {gol} gols.')
    print('-' * 45)
print('<< VOLTE SEMPRE >>')
