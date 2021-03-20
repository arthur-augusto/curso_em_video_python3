# Calcula uma distância em metros para outras unidades de medidas
distancia = float(input('Uma distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f'''A medida de {distancia:.1f}m corresponde a:
{km}km
{hm}hm
{dam}dam
{dm:.0f}dm
{cm:.0f}cm
{mm:.0f}mm
''')
