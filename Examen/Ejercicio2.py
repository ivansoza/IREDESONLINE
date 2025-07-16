n = int(input("Ingresa un número entero: "))

if n == 0:
    print("El número es cero y es par")
elif n > 0:
    if n % 2 == 0:
        print("El número es positivo y par")
    else:
        print("El número es positivo e impar")
else:
    if n % 2 == 0:
        print("El número es negativo y par")
    else:
        print("El número es negativo e impar")
