# Imprime na tela o primeiro e ultimo nome informado pelo usuário
nome_completo = str(input('Digite seu nome completo: ')).strip().split()
print(f'''Muito prazer em te conhecer!
Seu primeiro nome é {nome_completo[0]}
Seu último nome é {nome_completo[-1]}''')
