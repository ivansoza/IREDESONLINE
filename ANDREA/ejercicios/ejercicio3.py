
n = float(input('Número: '))

if n > 0:
    print('Positivo')
else:
    print('Negativo o Cero')

# Verifica si el número no tiene decimales
if n.is_integer():
    if int(n) % 2 == 0:
        print('Es par')
    else:
        print('Es impar')
else:
    print('Tiene decimales, no se puede saber si es par o impar')