#Crear un programa que pida un número entero e imprimirlo, si no ingresa deberá preguntar otra vez por el número entero hasta que ingrese un número positivo.

while True:
    entero = input("Ingrese número entero positivo: ")
    if not(entero.isdigit()):
        entero = input("Ingrese número entero positivo: ")
    elif int(entero)>0:
        print("Has ingresado un número entero positito correctamente")
        break


