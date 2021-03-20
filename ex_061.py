# Calcula os 10 primeiros valores de uma PA ultilizando o while
print('    Gerador de PA')
print('=' * 21)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 1
while contador != 11:
    print(f'{termo} -> ', end='')
    termo += razao
    contador += 1
print('FIM')
