# Recebe vários números inteiros enquanto o usuário não digita 999 e retorna a soma entre eles
soma = contador = 0
while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'A soma dos {contador} valores foi {soma}')
