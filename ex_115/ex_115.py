# Sistema em que é possível cadastrar pessoas e armazenar os cadastro em um arquivo .txt
from time import sleep
from lib import *
arq = 'cadastro.txt'
if not arquivo_existe(arq):
    criar_arquivo(arq)
while True:
    sleep(1)
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        ler_arquivo(arq)
    elif opcao == 2:
        titulo('NOVO CADASTRO')
        nome_usuario = str(input('Nome: '))
        idade_usuario = leia_int('Idade: ')
        cadastrar(arq, nome_usuario, idade_usuario)
    elif opcao == 3:
        break
    else:
        print(f"{cores('ERRO! Digite uma opção válida!', 'vermelho')}")
titulo('Saindo do sistema... Até logo!')
