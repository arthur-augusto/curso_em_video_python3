# Analisa se é possivel formar um triângulo a partir de 3 segmentos e qual o seu tipo
seg_a = float(input('Primeiro segmento: '))
seg_b = float(input('Segundo segmento: '))
seg_c = float(input('Terceiro segmento: '))
if seg_a < seg_b + seg_c and seg_b < seg_a + seg_c and seg_c < seg_a + seg_b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if seg_a == seg_b == seg_c:
        print('EQUILÁTERO!')
    elif seg_a == seg_b or seg_a == seg_c or seg_b == seg_c:
        print('ISÓCELES!')
    else:
        print('ESCALENO!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
