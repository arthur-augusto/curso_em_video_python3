# Separa as casas decimais de um número com quatro digitos
numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'''Analizando o número {numero}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}''')
