# Verifica a classificação de um atleta de acordo com a sua idade
from datetime import date
ano_nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - ano_nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
