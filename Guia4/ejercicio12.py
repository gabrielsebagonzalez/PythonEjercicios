"""12 - Análisis de palabra
Se pide un programa que le solicite al usuario que ingrese una palabra. Con esa palabra calcular
los siguientes puntos:
Determinar la cantidad de letras que tiene la palabra
Mostrar un mensaje que informe si la palabra termina en vocal"""

palabra = input("Ingrese una palabra: ").upper()

largo = len(palabra)
ultima_letra = palabra[largo - 1]
termina_vocal = False

if ultima_letra == "A" or ultima_letra == "E" or ultima_letra == "I" or ultima_letra == "O" or ultima_letra == "U":
    termina_vocal = True

print(f"La palabra ingresada tiene {largo} letras")
if termina_vocal:
    print("La palabra ingresada termina en vocal")

