# Verifica se a frase que o usuário digitou é um palíndromo
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
frase_reversa = '' # frade_reversa = frase[::-1]
for letra in range(len(frase) - 1, -1, -1):
    frase_reversa += frase[letra]
print(f'O inverso de {frase} é {frase_reversa}')
if frase == frase_reversa:
    print('Temos um palindromo!')
else:
    print('A frase digitada não é um palíndromo!')
