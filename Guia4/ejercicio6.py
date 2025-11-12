"""6 - Jornal de un Operario
Se necesita desarrollar un programa para el área de recursos humanos de una empresa que permita
informar el jornal de un determinado operario. Usted deberá cargar por teclado el código de turno
que el operario trabajó ese día (1- representa Diurno y 2- representa Nocturno) y la cantidad de horas
trabajadas.
La política de trabajo en la empresa es que los operarios de la misma pueden trabajar en el turno
diurno o nocturno. Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora, si lo
hace en el turno diurno cobra 35.50 pesos la hora."""

HORA_NOCTURNA = 40.60
HORA_DIURNA = 35.50

codigo_turno = int(input("Ingrese el turno de trabajo del operario (1- representa Diurno y 2- representa Nocturno): "))
cantidad_horas = float(input("Ingrese la cantidad de horas trabajadas: "))

if codigo_turno == 1:
    turno = "Diurno"
    salario = cantidad_horas * HORA_DIURNA
elif codigo_turno == 2:
    turno = "Nocturno"
    salario = cantidad_horas * HORA_NOCTURNA
else:
    print("Código de turno inválido")
    salario = 0
    turno = "Desconocido"

if codigo_turno > 0:
    print(f"El operario trabajó {cantidad_horas} horas en el turno {turno} y su salario es ${salario}")