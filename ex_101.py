# Mostra se uma pessoa tem voto negado, opcional ou obrigatório a partir de uma função
def voto(ano_nascimento):
    """
    A partir de um ano de nascimento calcula a idade atual da pessoa
    e retorna sua idade e condição de voto no Brasil
    :param ano_nascimento: ano de nascimento de uma pessoa
    :return: condição de voto (NEGADO, OPCIONAL ou OBRIGATÓRIO)
    """
    from datetime import date
    dados = {}
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    dados['idade'] = idade
    if idade < 16:
        dados['condição'] = 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        dados['condição'] = 'OPCIONAL'
    else:
        dados['condição'] = 'OBRIGATÓRIO'
    return dados


print('-=' * 30)
ano_usuario = int(input('Em que ano você nasceu? '))
dados_usuario = voto(ano_usuario)
print(f'Com {dados_usuario["idade"]} anos: VOTO {dados_usuario["condição"]}.')
