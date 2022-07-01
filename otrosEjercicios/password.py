clave = "Mycontraseña"



contador = 0

while contador<3:
    claveIngresada = input("Ingrese contraseña de su banco: ")
    if claveIngresada == clave:
        print("Clave correcata, bienvenido")
        break
    else:
        print("¡¡¡ ERROR !!!")
        contador+=1;