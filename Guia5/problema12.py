"""Problema 12.) Una compañía de alquiler de automóviles necesita un programa que calcule lo que se
debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el
automóvil:
i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500.
ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el
kilometraje excedente a los 300, a razón de $3 por kilómetro.
iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los
300, a razón de $1.5 por kilómetro."""

kilometros = int(input("Ingrese los kilómetros recorridos: "))

excedente = (kilometros - 300)

if kilometros <= 300:
    monto_total = 500

elif 300 < kilometros <= 1000:
    monto = excedente * 3
    monto_total = 500 + monto
else:
    monto = excedente * 1.5
    monto_total = 500 + monto

print(f"El cliente recorrió {kilometros}km debe abonar ${monto_total}")