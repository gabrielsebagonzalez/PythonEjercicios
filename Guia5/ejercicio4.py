"""4 - Mantenimiento informático
El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa
que facilite la gestión de las tareas realizadas en el día.
El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de identi
ficación de la PC, tiempo de reparación (expresado en minutos) y la causa de mantenimiento (1-
Problema de Hardware, 2-Problema de Software)
Los requerimientos funcionales son:
¿Cuál es el tiempo total de las tareas de mantenimiento?
¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?
Tiempo promedio de tareas de mantenimiento.
Informar con un mensaje si todas las PC a las que se les ha realizado mantenimiento tuvieron
problemas de hardware."""

num_identificacion_pc1 = int(input("Ingrese el número de identificación del PC1: "))
tiempo_rep_pc1 = int(input("Ingrese el tiempo de reparación expresado en minutos: "))
causa_pc1 = int(input("Ingrese la causa de mantenimiento, 1- Problema de Hardware, 2-Problema de Software: "))

num_identificacion_pc2 = int(input("Ingrese el número de identificación del PC2: "))
tiempo_rep_pc2 = int(input("Ingrese el tiempo de reparación expresado en minutos: "))
causa_pc2 = int(input("Ingrese la causa de mantenimiento, 1- Problema de Hardware, 2-Problema de Software: "))

num_identificacion_pc3 = int(input("Ingrese el número de identificación del PC3: "))
tiempo_rep_pc3 = int(input("Ingrese el tiempo de reparación expresado en minutos: "))
causa_pc3 = int(input("Ingrese la causa de mantenimiento, 1- Problema de Hardware, 2-Problema de Software: "))

tiempo_total = tiempo_rep_pc1 + tiempo_rep_pc2 + tiempo_rep_pc3

if tiempo_rep_pc1 > tiempo_rep_pc2 and tiempo_rep_pc1 > tiempo_rep_pc3:
    mayor_tiempo = num_identificacion_pc1, tiempo_rep_pc1
elif tiempo_rep_pc2 > tiempo_rep_pc1 and tiempo_rep_pc2 > tiempo_rep_pc3:
    mayor_tiempo = num_identificacion_pc2, tiempo_rep_pc2
else:
    mayor_tiempo = num_identificacion_pc3, tiempo_rep_pc3

tiempo_promedio = round(tiempo_total / 3, 2)

if causa_pc1 == 1 and causa_pc2 == 1 and causa_pc3 == 1:
    todas_hardware = True
else:
    todas_hardware = False

print()
print("*" * 10, "INFORME", "*" * 10)
print(f"El tiempo total de mantenimiento son {tiempo_total} minutos")
print(f"La PC con mayor tiempo de mantenimiento es la número: {mayor_tiempo[0]} con {mayor_tiempo[1]} minutos")
print(f"El tiempo promedio de las tareas de mantenimiento es: {tiempo_promedio} minutos")

if todas_hardware:
    print("todas las PC a las que se les ha realizado mantenimiento tuvieron problemas de hardware")
else:
    print("Las PC recibieron distintos tipos de mantenimiento")
