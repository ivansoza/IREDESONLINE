
edad = int(input('¿Qué edad tienes? '))

if edad < 13:
    print('Niño')
elif edad >= 13 and edad <= 17:
    print('Adolescente')
elif edad >= 18 and edad <= 59:
    print('Adulto')
else:
    print('Adulto mayor')
