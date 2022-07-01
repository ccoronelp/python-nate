nombre = input("Ingresa tu nombre: ")

contador = 0

for letra in nombre:
    contador += 1

print("Tu nombre tiene {} letras".format(contador))