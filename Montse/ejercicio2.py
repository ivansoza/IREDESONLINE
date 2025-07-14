

try:
    a = float(input('Número 1: '))
    b = float(input('Número 2: '))
except ValueError:
    print("Error: Entrada no válida, debes ingresar un número.")
    exit(1)

operador = input("Elige operación (+, -, *, /): ")

if operador == '+':
    print("Resultado:", a + b)
elif operador == '-':
    print("Resultado:", a - b)
elif operador == '*':
    print("Resultado:", a * b)
elif operador == '/':
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: División entre cero")
else:
    print("Operador no válido")
