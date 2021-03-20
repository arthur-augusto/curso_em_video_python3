# Verifica pela data de nascimento informada pelo usuário se ele precisa, se vai ou se ja passou o tempo do alistamento militar
from datetime import date
from math import fabs
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
ano_alistamento = ano_nascimento + 18
print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}')
if idade < 18:
    anos_faltam = ano_alistamento - ano_atual 
    print(f'Ainda faltam {anos_faltam} anos para o alistamento')
    print(f'Seu alistamento será em {ano_alistamento}.')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
else:
    anos_passados = ano_atual - ano_alistamento
    print(f'Você já deveria ter se alistado há {anos_passados} anos')
    print(f'Seu alistamento foi em {ano_alistamento}.')
