# Mostra um dicionário com vários cadastro a respeito das notas de um aluno
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dados = dict()
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    if sit:
        if dados['média'] < 5:
            dados['situação'] = 'RUIM'
        elif 5 <= dados['média'] < 7:
            dados['situação'] = 'RAZOÁVEL'
        else:
            dados['situação'] = 'BOA'
    return dados


print(notas(5.5, 2.5, 1.5, sit=True))
help(notas)
