# Analisa cadastro de várias pessoas
pessoas = []
dados = {}
soma_idade = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip()
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    pessoas.append(dados.copy())
    dados.clear()
    if opcao == 'N':
        break
n_pessoas = len(pessoas)
media_idade = soma_idade / n_pessoas
print('-=' * 30)
print(f'''A) Ao todos temos {n_pessoas} pessoas cadastradas.
B) A média de idade é de {media_idade:5.2f} anos.
C) As mulheres cadastradas foram ''', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print('\nD) Lista das pessoas que estão com a idade acima da média: ')
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'    nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<< ENCERRADO >>')
