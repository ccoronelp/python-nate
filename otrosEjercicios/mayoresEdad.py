listaEdades = []

while True:
    entero = input("Ingrese número de edades que desea ingresar: ")
    if not entero.isdigit():
        entero = input("Ingrese número de edades que desea ingresar: ")
    elif int(entero)<0:
        print("Por favor ingrese un número entero positivo")
    else:
        entero = int(entero)
        break

for num in range(entero):
    edad = input("Por favor ingresa la edad número {}: ".format(num+1))
    listaEdades.append(edad)
print("======================")

mayores = 0
for edad in listaEdades:
    if int(edad)>17:
        mayores+=1

print("Cantidad de mayores de edad: ", mayores)