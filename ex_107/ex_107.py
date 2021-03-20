# Mostra o resultado de várias funções do módulo moeda.py
import moeda

preco = float(input('Digite o preço: R$'))
print(f'''A metade de R${preco} é R${moeda.metade(preco)}
O dobro de R${preco} é R${moeda.dobro(preco)}
Aumentando 10%, temos R${moeda.aumentar(preco, 10)}''')
