#SOLUCIÓN AL RETO

n = float(input("Número: "))

print("Positivo" if n > 0 else "Negativo o Cero")

if n.is_integer():
    print("Es par" if int(n) % 2 == 0 else "Es impar")
else:
    print("No es un número entero, no se puede clasificar como par o impar.")
