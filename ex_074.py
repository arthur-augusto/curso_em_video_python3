# Sorteia 5 números e mostra o maior e menor entre eles
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sortados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'''\nO maior valor sorteado foi {max(numeros)}
O menor valor sorteado foi {min(numeros)}''')
