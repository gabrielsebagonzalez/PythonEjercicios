"""6 - Viaje Córdoba-Rosario
Un vehículo parte de la ciudad de Córdoba y se dirige a Rosario por autopista. La distancia aproximada
entre ambas ciudades es de 400 kilómetros. El vehículo se desplaza con velocidad promedio de
122 km/h.
Desarrolle un programa que calcule el tiempo total en horas que demorará ese vehículo en llegar a
Rosario. De nuevo, no es necesario convertir a horas, minutos y segundos: exprese en resultado como
un número real, tal cual lo haya obtenido del cálculo."""

distancia = 400
velocidadPromedio = 122

tiempoRecorrido = distancia / velocidadPromedio

print(f"El tiempo total es de: {tiempoRecorrido} hs")
