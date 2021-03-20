# Mini sitema para facilitar o uso do Interactive Help do Python
from time import sleep
cores = {'verde': '\033[0;42m',
         'azul': '\033[44m',
         'negativo': '\033[7m',
         'vermelho': '\033[41m'}


def ajuda(com):
    sleep(0.5)
    print_cores(f"Analisando o manual do comando '{comando}'", cor=cores['azul'])
    sleep(0.5)
    print(cores['negativo'], end='')
    help(com)


def print_cores(msg, cor='\033[m'):
    tamanho = len(msg) + 4
    print(cor, end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print('\033[m', end='')


while True:
    print_cores('SISTEMA DE AJUDA PyHELP', cor=cores['verde'])
    comando = input('Função ou Biblioteca > ')
    if comando.strip().upper() == 'FIM':
        break
    ajuda(comando)
sleep(0.5)
print_cores('ATÉ LOGO!', cor=cores['vermelho'])
