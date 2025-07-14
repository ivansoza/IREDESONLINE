

a = float(input("Número 1: "))
b = float(input("Número 2: "))
#print('Suma:', a + b)


operacion = input("Elige una operación (+, -, *, /): ")


if operacion == '+':
    print(f"Suma: {a + b}")
elif operacion == '-':
    print(f"Resta: {a - b}")
elif operacion == '*':
    print(f"Multiplicación: {a * b}")
elif operacion == '/':
    if b != 0:
        print(f"División: {a / b}")
    else:
        print("Error: no se puede dividir entre cero.")
else:
    print("Operación no válida.")
