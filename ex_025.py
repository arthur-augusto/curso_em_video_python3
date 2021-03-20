# Verifica se o nome do usuário possui silva
nome = str(input('Qual é o seu nome completo? ')).strip().lower()
silva = 'silva' in nome
print(f'Seu nome tem Silva? {silva}')
