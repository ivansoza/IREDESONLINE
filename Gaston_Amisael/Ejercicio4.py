#SOLUCIÓN AL RETO

ejercicio = input("Elige una operación(*,/,+,-):" )

a = float(input("Numero 1:"))
b = float(input("Numero 2:"))

if ejercicio == "*":
    print("El resultado es:", a * b)
elif ejercicio == "/":
    if b !=0:
        print("El resultado es:", a / b)
    else:
        print("No se puede dividir entre cero")
elif ejercicio == "+":
    print("El resultado es:", a + b)
elif ejercicio == "-":
    print("El resultado es:", a - b)
    


        