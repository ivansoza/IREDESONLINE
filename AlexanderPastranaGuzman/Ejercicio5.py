
texto = input("Escribe un texto: ")
conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
for c in texto.lower():
    if c in conteo_vocales:
        conteo_vocales[c] += 1


print("Conteo de vocales:")
for vocal, cantidad in conteo_vocales.items():
    print(f"{vocal}: {cantidad}")