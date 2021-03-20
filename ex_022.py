# Analisa o nome do usuário
nome_completo = str(input('Digite o seu nome completo: ')).strip()
nomes = nome_completo.split()
nomes_juntos = nome_completo.replace(' ', '')
print(f'''Analizando o seu nome...
Seu nome em maiúsculas é {nome_completo.upper()}
Seu nome em minúsculas é {nome_completo.lower()}
Seu nome tem ao todo {len(nomes_juntos)} letras
Seu primeiro nome é {nomes[0]} e ele tem {len(nomes[0])} letras
''')
