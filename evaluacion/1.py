try:#usar try para except ValueError . el try evita que el programa se rompa si el usuario escribe mal.
    # Solicitar un número al usuario
    n = float(input("Ingrese un número: "))

    if n > 0:
        print("El número es positivo.")
    elif n < 0:
        print("El número es negativo.")

        # reto agrga una condicion para verificar si el número es cero
    else:
        print("El número es cero.")

# si el usuasrio ingresa un caracter que no es un número, mandar un mensaje.

except ValueError:
    print("Error" " El carácter debe ser numérico.")
