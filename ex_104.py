# Recebe somente um número inteiro a partir de uma função
def leia_int(msg=''):
    while True:
        num = str(input(msg))
        if not num.isnumeric():
            print('\033[031mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return int(num)


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
