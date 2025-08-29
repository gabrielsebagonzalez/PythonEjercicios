"""3 - Cálculo de Regularidad
La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia
y mostrar si el alumno está libre, regular o promocionado. Las tres notas son los dos parciales más la
nota de prácticos y las condiciones de regularidad están descriptas a con􀆟nuación:
El promedio menor a 4 el alumno está libre
El promedio comprendido entre 4 y 8 el alumno está regular
El promedio mayor a 8 el alumno está promocionado."""

parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
nota_practico = float(input("Ingrese la nota del práctico: "))

promedio = round((parcial1 + parcial2 + nota_practico) / 3, 2)

if promedio < 4:
    condicion = "Libre"
elif 4 <= promedio <= 8:
    condicion = "Regular"
else:
    condicion = "Promocionado"
print(f"El promedio del alumno es: {promedio}")
print(f"La condición del alumno es: {condicion}")