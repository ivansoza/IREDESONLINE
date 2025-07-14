
entrada = input("Introduce los números separados por espacios: ")
numeros = [float(n) for n in entrada.split()]
prom = sum(numeros) / len(numeros)
print(f"Promedio: {prom}")



numeros_ordenados = sorted(numeros)
n = len(numeros_ordenados)

if n % 2 == 1:
    mediana = numeros_ordenados[n // 2]
else:
    medio1 = numeros_ordenados[n // 2 - 1]
    medio2 = numeros_ordenados[n // 2]
    mediana = (medio1 + medio2) / 2

print(f"Mediana: {mediana}")