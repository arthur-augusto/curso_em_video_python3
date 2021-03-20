# Módulo usado no ex_107
def metade(preco):
    metade_preco = preco / 2
    return metade_preco


def dobro(preco):
    dobro_preco = preco * 2
    return dobro_preco


def aumentar(preco, taxa):
    preco_aumentado = preco + (preco * taxa / 100)
    return preco_aumentado


def diminuir(preco, taxa):
    preco_diminuido = preco - (preco * taxa / 100)
    return preco_diminuido
