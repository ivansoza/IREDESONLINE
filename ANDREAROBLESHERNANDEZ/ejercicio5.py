
texto = input("Ingresa un texto: ").lower()

# Diccionario con las vocales
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# Contar cada vocal
for c in texto:
    if c in vocales:
        vocales[c] += 1

# Mostrar resultado
for v, cantidad in vocales.items():
    print(f"{v}: {cantidad}")
