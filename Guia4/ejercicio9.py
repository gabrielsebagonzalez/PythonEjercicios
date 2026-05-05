"""9 - Galería de Arte
Una galería de arte desea preparar un catálogo de sus cuadros más famosos. Se realiza una prueba
con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá verificar si
todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y
terminó en el año 2000). Determinar cuántos 􀆟enen an􀆟güedad inferior a 10 años. Si no hay ninguno,
imprimir el mensaje “Renovar stock”."""

ANIO_ACTUAL = 2026
anio_cuadro1 = int(input("Ingrese el año de creación del primer cuadro: "))
anio_cuadro2 = int(input("Ingrese el año de creación del segundo cuadro: "))
anio_cuadro3 = int(input("Ingrese el año de creación del tercer cuadro: "))

if anio_cuadro1 < 1901 and anio_cuadro2 < 1901 and anio_cuadro3 < 1901:
    print("Todas los cuadros son anteriores al siglo XX")
else:
    print("No todos los cuadros son anteriores al siglo XX")

contador_cuadros = 0

if ANIO_ACTUAL - anio_cuadro1 < 10:
    contador_cuadros += 1
if ANIO_ACTUAL - anio_cuadro2 < 10:
    contador_cuadros += 1
if ANIO_ACTUAL - anio_cuadro3 < 10:
    contador_cuadros += 1

if contador_cuadros == 0:
    print("Renovar stock")
else:
    print(f"Cantidad de cuadros con menos de 10 años de antiguedad: {contador_cuadros}")