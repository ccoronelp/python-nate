#Crear una función que permita verificar que un número de teléfono tenga 9 dígitos.

def telefono():
    while True:
        numero = input("Ingrese número telefónico sin espacios: ")
        if numero.isdigit() and len(numero) == 9:
            print("Número ingresado correctamente")
            break
        else:
            numero = input("Ingrese número telefónico sin espacios: ")


telefono()