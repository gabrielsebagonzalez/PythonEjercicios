"""Se solicita realizar un programa que permita generar tres temperaturas en forma aleatoria (correspondientes
a diferentes momentos de un día) y determinar:
Cuál es el promedio de las temperaturas
Si existe alguna temperatura que sea mayor al promedio"""
import random

temp1 = round(random.uniform(15.1, 45.9), 2)
temp2 = round(random.uniform(15.1, 45.9), 2)
temp3 = round(random.uniform(15.1, 45.9), 2)

promedio_temp = (temp1 + temp2 + temp3) / 3

print(f"El promedio de las temperaturas es: {promedio_temp}")

if (temp1 or temp2 or temp3) > promedio_temp:
    print("Existe alguna temperatura que es mayor al promedio")
else:
    print("Todas las temperaturas están por debajo del promedio")
