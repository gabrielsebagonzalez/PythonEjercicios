"""2 - Cuadrado de un binomio
Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores 𝑎 y
𝑏, que:
Un binomio al cuadrado (suma) esigual al cuadrado del primer término, más el doble producto del
primero por el segundo más el cuadrado del segundo."""

a = 4
b = 2

resultado = (a + b)**2
binomio = a**2 + 2*a*b + b**2

print(f"{resultado} = {binomio}")
