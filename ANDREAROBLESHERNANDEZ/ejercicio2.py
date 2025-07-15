
while True:
    print("\nCalculadora Básica")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ")

    if opcion == '5':
        print("¡Hasta luego!")
        break

    a = float(input('Número 1: '))
    b = float(input('Número 2: '))

    if opcion == '1':
        print(f'Suma: {a + b}')
    elif opcion == '2':
        print(f'Resta: {a - b}')
    elif opcion == '3':
        print(f'Multiplicación: {a * b}')
    elif opcion == '4':
        if b != 0:
            print(f'División: {a / b}')
        else:
            print('Error: No se puede dividir entre cero.')
    else:
        print("Opción no válida. Intenta de nuevo.")
