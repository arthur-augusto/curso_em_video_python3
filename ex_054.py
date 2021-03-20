# Verifica a maioridade de 7 pessoas a partir do ano de nascimento delas
from datetime import date
ano_atual = date.today().year
n_menores = 0
n_maiores = 0
for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade < 21:
        n_menores += 1
    else:
        n_maiores += 1
print(f'''Ao todo tivemos {n_maiores} pessoas maiores de idade
E também tivemos {n_menores} pessoas menores de idade''')
