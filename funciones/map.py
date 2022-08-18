#primer parámetro que irá en la función map es una función
def cuadrado(n):
    return n*n

#el segundo parámentro es nuestro elemento itinerable como una lista
numeritos = [1,2,3,4,5,6]

#ahora simplemente usamos la función map

resultado = map(cuadrado,numeritos)

#como podemos apreciar map devuelve un objeto tipo map
print(type(resultado))
#y para imprimirlo en consola tenemos que convertiro a lista
print(list(resultado))

