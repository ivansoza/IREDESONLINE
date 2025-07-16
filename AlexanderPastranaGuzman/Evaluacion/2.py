

n = int(input("Número entero: "))

if n % 2 == 0:
    print("Es par")
    if n % 4 == 0:
        print("Es multiplo de 4")
else:
    print("Es impar")
