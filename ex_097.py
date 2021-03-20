# Imprime 3 mensagens na tela com linhas proporcionais aos seus tamanhos
def escreva(msg):
    tamanho = len(msg) + 4
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
