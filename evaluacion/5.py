

# Ejemplo base:
# edad = int(input('¿Qué edad tienes? '))
# if edad < 18:
#     print('Eres menor de edad')
# else:
#     print('Eres mayor de edad')




# 5.py

edad = int(input('¿Qué edad tienes? '))

if edad < 13:
    print('Niño')
elif edad >= 13 and edad <= 17:
    print('Adolescente')
elif edad >= 18 and edad < 60:
    print('Adulto')
else:
    print('Adulto mayor')

