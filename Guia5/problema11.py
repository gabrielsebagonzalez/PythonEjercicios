"""Problema 11.) Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos. No
utilice para el proceso la función max() de la librería estándar de Python: diseñe el algoritmo
suponiendo que tal función no existe en el lenguaje que usará para el desarrollo del programa."""

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if num1 > num2 and num1 > num3:
    may = num1
elif num2 > num3:
    may = num2
else:
    may = num3

print(f"El número mayor es: {may}")