
nombre = input("Hola Como te llamas? ")

try:
    edad = int(input(f"{nombre}, ¿qué edad tienes? "))

    if edad < 0 or edad > 120:
        print("Esa no parece una edad valida. Intenta con un numero entre 0 y 120.")
    else:
        if edad < 13:
            print(f"{nombre}, eres un niño.")
        elif edad <= 17:
            print(f"{nombre}, eres un adolescente.")
        elif edad <= 59:
            print(f"{nombre}, eres un adulto.")
        else:
            print(f"{nombre}, eres un adulto mayor.")

        print("Gracias por usar el clasificador de edades.")
except ValueError:
    print("Por favor, ingresa un numero válido para la edad.")
