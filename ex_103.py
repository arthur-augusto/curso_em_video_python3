# Mostra a ficha de campeonata de um jogador
def ficha(nome_jogador='', n_gols=0):
    if nome_jogador == '':
        nome_jogador = '<desconhecido>'
    if type(n_gols) != int:
        n_gols = 0
    print(f'O jogador {nome_jogador} fez {n_gols} gol(s) no campeonato.')


nome = str(input('Nome do Jogador: ')).strip().title()
gols = input('Número de Gols: ')
ficha(nome, gols)
