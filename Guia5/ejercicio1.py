"""1 - Tirada de moneda
Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un
jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta."""
import random
caras = "cara", "cruz"
apuesta = int(input("Seleccione cara(0) o cruz(1): "))
jugada = random.choice(caras)

if jugada == caras[apuesta]:
    print(f"El jugador ha ganado el juego, salió {jugada}")
else:
    print(f"El jugador ha perdido el juego, salió {jugada} y el jugador eligió {caras[apuesta]}")