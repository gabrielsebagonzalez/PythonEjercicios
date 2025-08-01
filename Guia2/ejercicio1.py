"""1 - Cuadrados y cubos
Leer dos números y calcular:
La suma de sus cuadrados.
El promedio de sus cubos."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

sumaCuadrados = num1 ** 2 + num2 ** 2
cubos = num1 ** 3 + num2 ** 3
promedioCubos = cubos / 2

print(f"La suma de los cuadrados es: {sumaCuadrados}")
print(f"El promedio de los cubos es: {promedioCubos}")
