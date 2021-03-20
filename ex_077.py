# Mostra as vogais de uma palavra
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
