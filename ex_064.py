# Soma todos os valores que o usuário digitar enquanto ele não digitar 999
numero = soma = contador = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero != 999:
        soma += numero
        contador += 1
print(f'Você digitou {contador} números e a soma entre eles foi {soma}.')
