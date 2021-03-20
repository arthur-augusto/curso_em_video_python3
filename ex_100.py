# Sorteia uma lista com 5 números a partir de uma função e soma apenas os pares da lista a partir de outra função
from random import randint
from time import sleep


def sorteia(numeros):
    print('Sorteando 5 valores da lista: ', end='')
    for n in range(0, 5):
        numero = randint(1, 10)
        numeros.append(numero)
        print(f'{numero} ', end='', flush=True)
        sleep(0.5)
    print('PRONTO!')


def soma_par(numeros):
    pares = []
    for valor in numeros:
        if valor % 2 == 0:
            pares.append(valor)
    soma_pares = sum(pares)
    print(f'Somando os valores pares de {numeros}, temos {soma_pares}')


lista = []
sorteia(lista)
soma_par(lista)
