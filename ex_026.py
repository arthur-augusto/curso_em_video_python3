# Verifica quantas vezes a letra A apareceu e a posição da primeira e da última vez que ela apareceu
frase = str(input('Digite uma frase: ')).strip().lower()
print(f'''A letra A aparece {frase.count('a')} vezes na frase.
A primeira letra A apareceu na posição {frase.find('a')}
A última letra A apareceu na posição {frase.rfind('a') + 1}
''')
