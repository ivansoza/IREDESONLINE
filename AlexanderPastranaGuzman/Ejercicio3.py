
n = float(input("Número: "))
if n > 0:
    print("Positivo")
else:
    print("Negativo o Cero")
    

if n.is_integer():
    if int(n) % 2 == 0:
        print("Es par")
    else:
        print("Es impar")
else:
    print("No es un número entero, no se puede clasificar como par o impar.")
