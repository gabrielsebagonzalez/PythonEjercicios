"""4 - Últimos dígitos
¿Cómo usaría el operador resto (%) para obtener el valor del úl􀆟mo dígito de un número entero?
¿Y cómo obtendría los dos últimos dígitos? Desarrolle un programa que cargue un número entero por
teclado, y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)
[Ayuda: ¿cuáles son los posibles restos que se ob􀆟enen de dividir un número cualquiera por 10?]"""

print("*" * 10, "Ultimos dígitos de un número", "*" * 10)
num = int(input("Ingrese un número entero: "))

ultimoDigito = num % 10
ultimosDosDigitos = num % 100

print(f"El último dígito del número {num} es: {ultimoDigito}")
print(f"Los últimos dos dígitos del número {num} son {ultimosDosDigitos}")