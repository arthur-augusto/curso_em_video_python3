# Cadastro de pessoas
n_maiores = n_homens = n_mulheres_menores = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-' * 25)
    if idade >= 18:
        n_maiores += 1
    if sexo == 'M':
        n_homens += 1
    if idade < 20 and sexo == 'F':
        n_mulheres_menores += 1    
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opcao == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {n_maiores}
Ao todo temos {n_homens} homens cadastrados
E temos {n_mulheres_menores} mulheres menores de 20 anos''')
