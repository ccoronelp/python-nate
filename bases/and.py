# Usa el operador and para mostrar dependiendo de la edad ingresada
# si una persona está en la escuela, colegio o universidad

edad = int(input("Ingresa tu edad: "))

if edad < 5 or edad > 25:
    print("No estás estudiando")
if edad > 5 and edad < 12:  # tambien se puede usar una sola comparacion 5<edad<12
    print('Estas en la escuela')
if 12 < edad < 15:
    print("Estás en el colegio")
if 16 < edad < 25:
    print("Estas en la universidad")
