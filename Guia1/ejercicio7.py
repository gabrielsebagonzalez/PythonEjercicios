"""7 - Precio del boleto
Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia. Para el cálculo
del mismo se debe considerar el monto base (que se cobra siempre), más un valor extra calculado en
base a la cantidad de kilómetros a recorrer: Por cada kilómetro a recorrer se cobra $0,30 de adicional."""

montoBase = float(input("Ingrese el monto base: "))
kilometros = float(input("Ingrese los kilómetros a recorrer: "))
VALOR_EXTRA = 0.30

adicional = VALOR_EXTRA * kilometros
precio_total = montoBase + adicional

print(f"El total del boleto es: ${precio_total}")
