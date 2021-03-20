# Calcula a tabuada de vários números
while True:
    numero = int(input('Quer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    print('-' * 30)
    for n in range(1, 11):
        print(f'{numero} x {n:2} = {numero * n}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
