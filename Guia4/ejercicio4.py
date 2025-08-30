"""4 - Punto en el plano
Se pide realizar un programa que ingresando el valor x e y de un punto determine a qué cuadrante
pertenece en el sistema de coordenadas."""

x = float(input("Ingrese el punto x: "))
y = float(input("Ingrese el punto y: "))

if x == 0 or y == 0:
    cuadrante = "Alguno de los ejes o el origen"
elif x > 0 and y > 0:
    cuadrante = "Primer cuadrante"
elif x < 0 < y:
    cuadrante = "Segundo cuadrante"
elif x < 0 and y < 0:
    cuadrante = "Tercer cuadrante"
else:
    cuadrante = "Cuarto cuadrante"

print(f"Los puntos {x} y {y} se encuentran ubicados en {cuadrante}")

