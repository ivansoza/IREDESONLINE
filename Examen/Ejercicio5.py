edad = float(input("Ingresa tu edad: "))

if edad <= 3:
    print("Eres un bebé")
elif edad > 3 and edad <= 12:
    print("Eres un niño")
elif edad > 12 and edad <= 19:
    print("Eres un adolescente")
elif edad > 19 and edad <= 30:
    print("Eres un joven")
elif edad > 30 and edad <= 65:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


#RETO AGREGAR EDADES