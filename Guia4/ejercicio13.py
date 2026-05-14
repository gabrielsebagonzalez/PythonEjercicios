"""13 - ¿Piedra, Papel o Tijera?
Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra,
papel o tijera” y determine cuál de ellos es el ganador. Las reglas son:
La piedra aplasta (o rompe) la tijera. (Gana la piedra).
La tijera corta el papel. (Gana la tijera).
El papel envuelve la piedra. (Gana el papel)
Si los dos jugadores eligen el mismo elemento, empatan."""
import random

jugador = input("Ingrese PIEDRA, PAPEL O TIJERA: ").upper()
elementos = ("PIEDRA", "PAPEL", "TIJERA")
maquina = random.choice(elementos)
print(f"Máquina elije {maquina}")

if jugador == maquina:
    resultado = "Empataron"
else:
    if (maquina == "PIEDRA" and jugador == "TIJERA") or (maquina == "TIJERA" and jugador == "PAPEL") or \
            (maquina == "PAPEL" and jugador == "PIEDRA"):
        resultado = "Gana máquina"
    else:
        resultado = "Gana Jugador"

print(resultado)

