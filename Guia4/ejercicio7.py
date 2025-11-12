"""7 - Comercio
Un comerciante tiene a la venta 3 tipos de articulos principales. Conociendo la cantidad vendida
de cada artículo y el precio unitario de cada artículo, hacer un programa que determine cuál fue el
producto que realizó el mayor aporte en los ingresos y el porcentaje que dicho aporte significa en el
ingreso absoluto de los 3 articulos sumados. Ese porcentaje se calcula así:
Absoluto = 100 %
Mayor aporte = 𝑥 %
Por lo tanto: 𝑥 = Mayor aporte"""

print("Comercio")
print("Carga de artículos vendidos")
print("=" * 40)

nombre_articulo1 = input("Ingrese el nombre del artículo 1: ")
cant_articulo1 = int(input("Ingrese la cantidad vendida del artículo 1: "))
precio_articulo1 = float(input("Ingrese el precio unitario del artículo 1: "))

nombre_articulo2 = input("Ingrese el nombre del artículo 2: ")
cant_articulo2 = int(input("Ingrese la cantidad vendida del artículo 2: "))
precio_articulo2 = float(input("Ingrese el precio unitario del artículo 2: "))

nombre_articulo3 = input("Ingrese el nombre del artículo 3: ")
cant_articulo3 = int(input("Ingrese la cantidad vendida del artículo 3: "))
precio_articulo3 = float(input("Ingrese el precio unitario del artículo 3: "))

ventas_articulo1 = cant_articulo1 * precio_articulo1
ventas_articulo2 = cant_articulo2 * precio_articulo2
ventas_articulo3 = cant_articulo3 * precio_articulo3

if ventas_articulo1 > ventas_articulo2 and ventas_articulo1 > ventas_articulo3:
    mayor_venta = nombre_articulo1, ventas_articulo1

elif ventas_articulo2 > ventas_articulo1 and ventas_articulo2 > ventas_articulo3:
    mayor_venta = nombre_articulo2, ventas_articulo2

else:
    mayor_venta = nombre_articulo3, ventas_articulo3


print(f"El artículo que mayor aporte realizó fué {mayor_venta[0]} con ganancias de ${mayor_venta[1]}")

total = ventas_articulo1 + ventas_articulo2 + ventas_articulo3
porcentaje = (mayor_venta[1] * 100) / total

print(f"y representa el {round(porcentaje, 2)}% del total ${total} de ingresos")




