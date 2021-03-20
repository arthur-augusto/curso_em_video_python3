# Recebe o nome, idade e o sexo de 4 pessoas e imprime na tela informações do grupo
soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''
n_mulheres_novas = 0
for pessoa in range(1, 5): # Recebe o nome, idade e sexo 4 vezes
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idades += idade # Soma todas as idades para fazer a média
    if sexo == 'M' and idade > idade_mais_velho: # Recebe o nome e a idade do homem mais velho
        idade_mais_velho = idade
        nome_mais_velho = nome
    if sexo == 'F' and idade < 20: # Conta o número de mulheres menores de 20 anos
        n_mulheres_novas += 1
media_idade = soma_idades / 4 # Calcula a média de idade do grupo
print(f'''A média de idade do grupo é de {media_idade} anos.
O homem mais velho tem {idade_mais_velho} anos e se chama {nome_mais_velho}.
Ao todo são {n_mulheres_novas} mulheres com menos de 20 anos.
''')
