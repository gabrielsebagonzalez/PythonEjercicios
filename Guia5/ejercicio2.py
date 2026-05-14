"""2 - Operaciones de orden con tres números
Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es
el resto de la división de los dos primeros."""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    mayor = num1
    if num2 > num3:
        medio = num2
        menor = num3
    else:
        medio = num3
        menor = num2

elif num2 > num1 and num2 > num3:
    mayor = num2
    if num1 > num3:
        medio = num1
        menor = num3
    else:
        medio = num3
        menor = num1

else:
    mayor = num3
    if num2 > num1:
        medio = num2
        menor = num1
    else:
        medio = num1
        menor = num2

if menor == mayor % medio:
    print("El tercero es igual al resto de la división de los dos primeros")
else:
    print("El tercero NO es igual al resto de la división de los dos primeros")


