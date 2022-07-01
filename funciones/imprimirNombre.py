#5.	Cree una función llamada saludo, que reciba como parámetro el nombre y apellido e imprime: “Hola me llamo NOMBRE y tengo la edad 38.

def saludo(nombre, apellido):
    print("Hola me llamo {} {} y tengo 38".format(nombre, apellido))


nombre = input("Ingresa nombre: ")
apellido = input("Ingresa apellido: ")


saludo(nombre,apellido)