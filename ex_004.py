# Informa ao usuário varias características do que ele digitou
entrada = input('Digite algo: ')
tipo = type(entrada)
espacos = entrada.isspace()
numero = entrada.isnumeric()
alfabetico = entrada.isalpha()
alfanumerico = entrada.isalnum()
maiuscula = entrada.isupper()
minuscula = entrada.islower()
capitalizada = entrada.istitle()
print(f'''O tipo primitivo desse valor é {tipo}
Só tem espaços? {espacos}
É um número? {numero}
É alphabético? {alfabetico}
É alfanúmerico? {alfanumerico}
Está em maiúsculas? {maiuscula}
Está em minúsculas? {minuscula}
Está capitalizada? {capitalizada}
''')
