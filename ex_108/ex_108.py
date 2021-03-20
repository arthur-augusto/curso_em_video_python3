# Aprimora o ex_107 formatando a moeda usada em preço
import moeda

preco = float(input('Digite o preço: R$'))
print(f'''A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}
O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}
Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}''')
