# Converte um número inteiro para binario, octal ou hexadecimal de acordo com a escolha do usuário
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}') # bin(num).replace('0b', '')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}') # oct(num).replace('0o', '')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}') # hex(num).replace('0x', '')
else:
    print('OPÇÃO INVÁLIDA!')
