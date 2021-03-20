# Recebe um valor inteiro e real do usuário e caso ele informe um valor errado recebe novamente
def leia_int(msg=''):
    while True:
        try:
            z = int(input(msg))
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número inteiro válido.\033[m')
        else:
            return z


def leia_float(msg=''):
    while True:
        try:
            r = float(input(msg))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor, digite um número real válido.\033[m')
        else:
            return r


inteiro = leia_int('Digite um Inteiro: ')
real = leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
