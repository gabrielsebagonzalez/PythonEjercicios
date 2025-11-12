"""Desarolle un programa completo en python, sin usar las funciones predefinidas min() y max(), que permita cargar
 por teclado dos números. Determine y muestre el mayor, el cuadrado del mayor y el cubo del mayor"""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    mayor = num1
else:
    mayor = num2

cuadrado = mayor ** 2
cubo = mayor ** 3

print(f"El mayor es {mayor}")
print(f"El cuadrado de {mayor} es: {cuadrado}")
print(f"El cubo de {mayor} es: {cubo}")
