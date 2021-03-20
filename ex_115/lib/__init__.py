# Pacote de interface do ex_115
def linha(forma='-', tamanho=42):
    print(forma * tamanho)


def titulo(msg, forma='-', tamanho=42):
    str(msg)
    linha(forma, tamanho)
    print(msg.center(tamanho))
    linha(forma, tamanho)


def cores(msg, cor='normal'):
    tipos = {'normal': '\033[m',
             'vermelho': '\033[31m',
             'verde': '\033[32m',
             'amarelo': '\033[33m',
             'azul': '\033[34m',
             'roxo': '\033[35m',
             'ciano': '\033[36m',
             'cinza': '\033[37m'}
    return f"{tipos[cor]}{msg}{tipos['normal']}"


def leia_int(msg=''):
    while True:
        try:
            z = int(input(msg))
        except KeyboardInterrupt:
            print(cores('\nUsuário preferiu não digitar esse número.', 'vermelho'))
            return 0
        except (ValueError, TypeError):
            print(cores('ERRO! Por favor, digite um número inteiro válido.', 'vermelho'))
        else:
            return z


def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f"{cores(c, 'amarelo')} - {cores(item, 'azul')}")
        c += 1
    linha()
    opcao = leia_int(cores('Sua opção: ', 'verde'))
    return opcao


def arquivo_existe(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Aquivo {arquivo} criado com sucesso!')


def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arquivo.close()
