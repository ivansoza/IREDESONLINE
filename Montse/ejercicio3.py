

# Ejemplo base
n = float(input('Número: '))

if n > 8:
    print('Positivo')
elif n == 0:
    print('Cero')
else:
    print('Negativo')

# Reto: verificar si es par o impar solo si es entero
if n.is_integer():
    if int(n) % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
else:
    print("No es entero, no se puede determinar si es par o impar")
