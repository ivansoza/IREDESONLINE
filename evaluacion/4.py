


#calificacion aprobatoria

nota = float(input("Ingrese una calificación: "))

# definir el rango de notas del 0 al 10
if nota < 0 or nota > 10:
    print("Nota incorrecta. Debe estar entre 0 y 10.")
else:
    if nota >= 6:
        print("APROBADO.")
    else:
        print("REPROBADO.")

    # Reto: agregar más categorías
    if nota == 10:
        print("EXCELENTE.")
    elif nota >= 8:
        print("MUY BUENO.")
    elif nota >= 7:
        print("BUENO.")
    elif nota >= 6:
        print("SUFICIENTE.")
    else:
        print("INSUFICIENTE.")
