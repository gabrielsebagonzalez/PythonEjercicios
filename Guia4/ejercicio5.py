"""5 - Postulantes a un empleo
Se tienen los datos de tres postulantes a un empleo, a los que se les realizó un test de capacitación.
Por cada postulante, se tiene entonces la siguiente información: nombre del postulante, cantidad total
de preguntas que se le realizaron y cantidad de preguntas que contestó correctamente.
Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de cada
uno según los criterios de aprobación que se indican más abajo, e indique finalmente el nombre del
postulante que ganó el puesto. Los criterios de aprobación son los siguientes, en función del porcentaje
de respuestas correctas sobre el total de preguntas realizadas a cada postulante:
Nivel Superior: Porcentaje 90 %
Nivel Medio: 75 % Porcentaje < 90 %
Nivel Regular: 50 % Porcentaje < 75 %
Fuera de Nivel: Porcentaje < 50 %"""

nom_postulante1 = input("Ingrese el nombre del primer postulante: ")
total_preguntas1 = int(input("Ingrese el total de preguntas realizadas: "))
preguntas_correctas1 = int(input("Ingrese la cantidad de preguntas correctas: "))

nom_postulante2 = input("Ingrese el nombre del segundo postulante: ")
total_preguntas2 = int(input("Ingrese el total de preguntas realizadas: "))
preguntas_correctas2 = int(input("Ingrese la cantidad de preguntas correctas: "))

nom_postulante3 = input("Ingrese el nombre del tercer postulante: ")
total_preguntas3 = int(input("Ingrese el total de preguntas realizadas: "))
preguntas_correctas3 = int(input("Ingrese la cantidad de preguntas correctas: "))

porcentaje1 = preguntas_correctas1/total_preguntas1 * 100
porcentaje2 = preguntas_correctas2/total_preguntas2 * 100
porcentaje3 = preguntas_correctas3/total_preguntas3 * 100

if porcentaje1 > 90:
    nivel_post1 = "Nivel Superior"
elif 75 <= porcentaje1 < 90:
    nivel_post1 = "Nivel medio"
elif 50 <= porcentaje1 < 75:
    nivel_post1 = "Nivel Regular"
else:
    nivel_post1 = "Fuera de Nivel"

if porcentaje2 > 90:
    nivel_post2 = "Nivel Superior"
elif 75 <= porcentaje2 < 90:
    nivel_post2 = "Nivel medio"
elif 50 <= porcentaje2 < 75:
    nivel_post2 = "Nivel Regular"
else:
    nivel_post2 = "Fuera de Nivel"

if porcentaje3 > 90:
    nivel_post3 = "Nivel Superior"
elif 75 <= porcentaje3 < 90:
    nivel_post3 = "Nivel medio"
elif 50 <= porcentaje3 < 75:
    nivel_post3 = "Nivel Regular"
else:
    nivel_post3 = "Fuera de Nivel"

if porcentaje1 > porcentaje2 and porcentaje1 > porcentaje3:
    postulante_ganador = nom_postulante1
    mayor_nivel = nivel_post1
    mayor_porcentaje = porcentaje1
elif porcentaje2 > porcentaje1 and porcentaje2 > porcentaje3:
    postulante_ganador = nom_postulante2
    mayor_nivel = nivel_post2
    mayor_porcentaje = porcentaje2
else:
    postulante_ganador = nom_postulante3
    mayor_nivel = nivel_post3
    mayor_porcentaje = porcentaje3

print(f"El postulante ganador es {postulante_ganador} con un porcentaje de {mayor_porcentaje} % con\
{mayor_nivel}")