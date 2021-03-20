# Verifica se o número que o usuário digitou é impar ou par
numero = int(input('Me diga um número qualquer: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR')
else:
    print(f'O número {numero} é ÍMPAR')
