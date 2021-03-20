# Verifica se é possivel formar um triângulo a partir dos 3 segmentos que o usuário digitou
print('-=' * 30)
print('                  Analisador de Triângulos')
print('-=' * 30)
seg_a = float(input('Primeiro segmento: '))
seg_b = float(input('Segundo segmento: '))
seg_c = float(input('Terceiro segmento:'))
if seg_a < seg_b + seg_c and seg_b < seg_a + seg_c and seg_c < seg_a + seg_b:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
