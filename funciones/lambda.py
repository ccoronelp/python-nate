#función que obtiene el cuadrado de un número

def cuadrado(num):
    return num**2

#funcion lambda que obtiene el cuadrado de un número:

cuadra = lambda x: x**2

#como podemos apreciar la función no tiene nombre

print (cuadrado(4))
print (cuadra(3))

#lambda se puede usar con map() y con filter()
numbers = [1,2,3,4,5,6,7,8]

#elevamos al cuadrado
mNumbers = map(lambda x: x**2,numbers)
#aquí lo que estamos haciendo es pasar la lista de números y
#elevarlo al cuadrado cada uno de ellos
print(list(mNumbers))

#******
#lamnda con filter()
fNumbers = filter(lambda x:x%2==0,numbers)
#estamos pasando la lista de números para que filter aplique la 
#función lamnda que verifica si el número es par,
# filter retornará solo los valores que sean verdaderos
print(list(fNumbers))