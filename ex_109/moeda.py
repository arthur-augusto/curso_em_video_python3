# Módulo usado no ex_107 com a adição da função moeda como parametro para as outras funções
def metade(preco=0, moeda_formatada=False):
    metade_preco = preco / 2
    if moeda_formatada:
        return moeda(metade_preco)
    else:
        return metade_preco


def dobro(preco=0, moeda_formatada=False):
    dobro_preco = preco * 2
    if moeda_formatada:
        return moeda(dobro_preco)
    else:
        return dobro_preco


def aumentar(preco=0, taxa=100, moeda_formatada=False):
    preco_aumentado = preco + (preco * taxa / 100)
    if moeda_formatada:
        return moeda(preco_aumentado)
    else:
        return preco_aumentado


def diminuir(preco=0, taxa=100, moeda_formatada=False):
    preco_diminuido = preco - (preco * taxa / 100)
    if moeda_formatada:
        return moeda(preco_diminuido)
    else:
        return preco_diminuido


def moeda(preco=0, tipo_moeda='R$'):
    return f'{tipo_moeda}{preco:.2f}'.replace('.', ',')
