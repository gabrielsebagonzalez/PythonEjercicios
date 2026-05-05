"""11 - Tarjeta de Bingo
Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100, que representaria
la tarjeta de bingo de una persona. Una vez generado los numeros aleatorios solicitar al
usuario que ingrese 3 numeros enteros, a par􀆟r de alli mostrar los siguientes mensajes:
Si el usuario no marco ninguno de los numeros indicarlo diciendo “El jugador 􀆟ene mala suerte,
no marco ninguna casilla”.
Caso contrario mostrar “El jugador marco algún número de la tarjeta”."""
import random

tarjeta = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100), random.randint(1, 100), random.randint(1, 100),
            random.randint(1, 100),random.randint(1, 100), random.randint(1, 100))

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

print(f"La tarjeta del usuario es: {tarjeta}")
if (num1 or num2 or num3) not in tarjeta:
    print("El jugador tiene mala suerte, no marcó ninguna casilla")
else:
    print("El jugador marco algún número de la tarjeta")