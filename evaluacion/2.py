

#numero es par o o impar

n = int(input("Ingrese un número entero: "))

if n % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

    #reto verifica si el numero es multiplo de 4 y mostrar el multiplo de 4 en ese caso
if n % 4 == 0:
    print(f"El número {n} es múltiplo de 4.")

    #reto verifica si el numero es multiplo de 3, 5, 7, 8, 9 y 10
    
if n.is_integer():
    entero = int(n)
    print(f"Multiplo del numero ingresado")
    for i in range(3, 11):
        if entero % i == 0:
            print(f"{entero} es múltiplo de {i}.")

            