# Informa o maior e o menor valor entre os 3 que o usuário digitou
numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
numero3 = int(input('Terceiro valor: '))
menor = numero1
maior = numero1
if numero2 < numero1 and numero2 < numero3:
    menor = numero2
if numero3 < numero1 and numero3 < numero2:
    menor = numero3
if numero2 > numero1 and numero2 > numero3:
    maior = numero2
if numero3 > numero1 and numero3 > numero2:
    maior = numero3
print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
