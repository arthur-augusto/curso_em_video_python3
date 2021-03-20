# Módulo para a validação de cadastro
def leia_dinheiro(msg):
    valido = False
    while not valido:
        preco = str(input(msg).replace(',', '.')).strip()
        if preco.isalpha() or preco.isspace() or preco == '':
            print(f'\033[31mERRO! "{preco}" é um preço inválido!\033[m')
        else:
            valido = True
            return float(preco)
