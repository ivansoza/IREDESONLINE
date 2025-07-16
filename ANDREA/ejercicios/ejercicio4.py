
entrada = input("Ingresa números separados por espacios: ")
numeros = [float(n) for n in entrada.split()]

# Calcular promedio
prom = sum(numeros) / len(numeros)
print("Promedio:", prom)

# Calcular mediana
ordenados = sorted(numeros)
n = len(ordenados)

if n % 2 == 1:
    mediana = ordenados[n // 2]
else:
    mediana = (ordenados[n // 2 - 1] + ordenados[n // 2]) / 2

print("Mediana:", mediana)