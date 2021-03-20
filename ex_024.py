# Verifica se a cidade em que o usuário nasce começa com a palavra santo
cidade = str(input('Em que cidade você nasceu? ')).strip().upper().split()
print('SANTO' in cidade[0])
