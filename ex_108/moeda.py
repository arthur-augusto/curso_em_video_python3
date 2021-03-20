# Módulo usado no ex_107 com a adição da função moeda
def metade(preco=0):
    metade_preco = preco / 2
    return metade_preco


def dobro(preco=0):
    dobro_preco = preco * 2
    return dobro_preco


def aumentar(preco=0, taxa=100):
    preco_aumentado = preco + (preco * taxa / 100)
    return preco_aumentado


def diminuir(preco=0, taxa=100):
    preco_diminuido = preco - (preco * taxa / 100)
    return preco_diminuido


def moeda(preco=0, tipo_moeda='R$'):
    return f'{tipo_moeda}{preco:.2f}'.replace('.', ',')
