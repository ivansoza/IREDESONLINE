


edad = int(input("¿Qué edad tienes? "))

# Clasificación por edad
if edad < 0:
    print("Edad inválida.")

    # reto  clasificación por edad niño, adolescente, adulto, adulto mayor
elif edad < 13:
    print("Eres un niño.")
elif edad < 18:
    print("Eres un adolescente.")
elif edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

    

