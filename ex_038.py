# Compara 2 valores e informa qual dos dois é maior ou se eles são iguais
numero1 = float(input('Primeiro número: '))
numero2 = float(input('Segundo número: '))
if numero1 > numero2:
    print('O PRIMEIRO valor é maior')
elif numero2 > numero1:
    print('O SEGUNDO valor é maior')
else:
    print('Os dois valores são IGUAIS')
