

# Ejemplo base
numeros = [8, 3, 9, 1]
prom = sum(numeros) / len(numeros)
print('Promedio:', prom)

# Reto
entrada = input("Ingresa números separados por espacio: ")
numeros = [float(x) for x in entrada.split()]

prom = sum(numeros) / len(numeros)
print("Promedio:", prom)

# Mediana
numeros_ordenados = sorted(numeros)
n = len(numeros_ordenados)
if n % 2 == 1:
    mediana = numeros_ordenados[n // 2]
else:
    mediana = (numeros_ordenados[n // 2 - 1] + numeros_ordenados[n // 2]) / 2
print("Mediana:", mediana)
