

# Ejemplo base
texto = 'Hola mundo'
vocales = 0
for c in texto.lower():
    if c in 'aeiou':
        vocales += 1
print('Total de vocales:', vocales)

# Reto
texto = input("Escribe un texto: ")
conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for c in texto.lower():
    if c in conteo:
        conteo[c] += 1

for vocal, cantidad in conteo.items():
    print(f"{vocal}: {cantidad}")
