# Mostra cadastro sobre a carteira de trabalho do usário
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip()
ano_nascimento = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - ano_nascimento
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
    print(f'    - {k} tem valor {v}')
