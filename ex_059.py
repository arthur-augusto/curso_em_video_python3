# Dados 2 valores o usuário pode somar, multiplicar ou mostrar o maior valor quantas vezes ele desejar
from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual a sua opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} + {valor2} é {soma}')
    elif opcao == 2:
        produto = valor1 * valor2
        print(f'O resultado de {valor1} x {valor2} é {produto}')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'Entre {valor1} e {valor2} o maior é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Oção inválida. Tente novamente.')
    sleep(2)
    print('-=' * 30)
print('Fim do programa! Volte sempre!')
