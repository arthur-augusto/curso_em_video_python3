# Calcula a média entre duas notas de um aluno e mostra se ele foi reprovado, ficou de recuperação ou aprovado
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if media < 5:
    print('O aluno está REPROVADO.')
elif 5 <= media < 7:
    print('O aluno está em RECUPERAÇÃO.')
elif media >= 7:
    print('O aluno está APROVADO')
