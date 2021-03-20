# Mostra a média e as notas de vários alunos
alunos = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    dados = [nome, nota1, nota2]
    alunos.append(dados[:])
    dados.clear()
    while True:
        opcao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if opcao in 'SN':
            break
    if opcao == 'N':
        break
print('-=' * 30)
print(f'No.   NOME{"MÉDIA":>20}')
print('-' * 30)
for a in range(0, len(alunos)):
    media = (alunos[a][1] + alunos[a][2]) / 2
    print(f'{a:<6}{alunos[a][0]:<20}{media:>4.1f}')
while True:
    print('-' * 30)
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno == 999:
        break
    if aluno <= len(alunos) -1:
        print(f'As notas de {alunos[aluno][0]} são {alunos[aluno][1:]}')
print('FINALIZANDO...')
print(f'{" VOLTE SEMPRE ":-^30}')
