"""2 - Impuesto Automotor
Crear un programa que permita calcular los impuestos que debe pagar un auto, conociendo su
modelo (año de fabricación) y tipo (P: Particular/T: Taxi/R: Remis). Para calcular los impuestos, tener
en cuenta que:
Los autos particulares de menos de 10 años de antigüedad pagan $200, entre 10 y 20 años pagan
$150 y no pagan impuestos los que tienen más de 20 años.
Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.
Los remises pagan $100 por cada año de antigüedad de su vehículo"""

modelo = int(input("Ingrese el modelo de su vehículo: "))
tipo = input("Ingrese una letra para el tipo (P: Particular/T: Taxi/R: Remis): ").upper()
FECHA_ACTUAL = 2025

antiguedad = FECHA_ACTUAL - modelo

if tipo == "P" or  tipo == "T":
    if antiguedad < 10:
        impuesto = 200
    if antiguedad < 20:
        impuesto = 150
    else:
        impuesto = 0
    if tipo == "T":
        impuesto = impuesto + 150
else:
    impuesto = 100 * antiguedad

print(f"El vehículo debe abonar ${impuesto}")



