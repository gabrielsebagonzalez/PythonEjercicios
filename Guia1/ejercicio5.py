"""5 - Conversión de medidas
Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
yardas
pulgadas
centimetros
metros
Sabiendo que:
1 pie = 12 pulgadas
1 yarda = 3 pies
1 pulgada = 2.54 centimetros
1 metro = 100 centimetros"""

medidaEnPie = int(input("Ingrese la medida en pies: "))

yardas = medidaEnPie / 3
pulgadas = medidaEnPie * 12
centimetros = pulgadas * 2.54
metros = centimetros / 100

print(f"La medida {medidaEnPie} pies equivale a {yardas} yardas {pulgadas} pulgadas {centimetros} centimetros {metros} metros")
