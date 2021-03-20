# Verifica se uma expressão é válida ou não
expressao = str(input('Digite uma expressão: ')).strip()
parenteses = []
for e in expressao:
    if e == '(':
        parenteses.append('(')
    elif e == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
