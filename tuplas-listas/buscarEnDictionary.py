#5.	Del diccionario anterior verifica si el cliente tiene como deporte favorito básquetbol e imprime “Eres un buen jugador de básquet”.

#Creamos un diccionario demo para ver qué estructura tendrá nuestro diccionario
demoDictionary = {
    'nombre': "Pepito",
    'apellido': "Flores",
    'edad': 18,
    #ahora agregamos una lista dentro del diccionario
    'deportes_favoritos' : [
        "Fútbol","natación"
    ]
}

#Recolectamos datos

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")
edad = int(input("Ingrese edad: "))

num_deportes = int(input("¿Cuántos deportes favoritos desea ingresar? "))
deportes_favoritos = []

for indice in range(num_deportes):
    deporte = input("Ingrese su deporte favorito número {}: ".format(indice+1))
    deportes_favoritos.append(deporte)

#Creamos el diccionario
diccionario = {}

#Agregamos los datos al diccionario con la función setdefault
diccionario.setdefault("nombre", nombre)
diccionario.setdefault("apellido",apellido)
diccionario.setdefault("edad",edad)
diccionario.setdefault("deportes_favoritos",deportes_favoritos)

#Buscando algo en el diccionario
for indice in diccionario["deportes_favoritos"]:
    if indice == "básquetbol":
        print("Eres un buen jugador de básquet")
    else:
        print("No juegas Baloncesto")