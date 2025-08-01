"""2 - Descuento en medicinas
Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia (cargar
por teclado el precio de ese medicamento) sabiendo que todos los medicamentos tienen un descuento
del 35 %.
Mostrar el precio actual, el monto del descuento y el monto final a pagar."""

precioMedicamento = float(input("Ingrese el precio del medicamento: "))
print()
DESCUENTO = 35

montoDescuento = precioMedicamento * 0.35
precioFinal = precioMedicamento - montoDescuento

print(f"El precio actual del medicamento es: ${precioMedicamento}")
print(f"El monto del descuento es: ${montoDescuento}")
print(f"El precio final del medicamento es: ${precioFinal}")