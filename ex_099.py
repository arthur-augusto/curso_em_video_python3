# Mostra na tela o maior entre vários parametros
from time import sleep


def maior(*numeros):
    print('-=' * 30)
    if numeros == ():
        numeros = 0
        n_valores = 0
        maior_valor = 0
    else:
        n_valores = len(numeros)
        maior_valor = max(numeros)
    print('Analisando os valores passados...')
    if numeros == 0:
        print('Foram informados 0 valores ao todo.')
    else:
        for n in numeros:
            print(f'{n} ', end='')
            sleep(0.5)
        print(f'foram informados {n_valores} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
