# Recebe quantos valores o usuário desejar e no fim mostra o número de valores digitados, a média entre eles e o maior e menor valor
opcao = ''
contador = soma = maior = menor = 0
while opcao != 'N':
    print('-' * 25)
    numero = int(input('Digite um número: '))
    opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / contador
print(f'''Você digitou {contador} números e a média foi {media}
O maior valor foi {maior} e o menor foi {menor}.''')
