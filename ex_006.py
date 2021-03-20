# Mostra o dobro, o triplo e a raiz quadrada do número que o usuário digitou
numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print(f'''O dobro de {numero} vale {dobro}.
O triplo de {numero} vale {triplo}.
A raiz quadrada de {numero} é igual a {raiz:.2f}.
''')
