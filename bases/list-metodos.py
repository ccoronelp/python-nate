#vamos a repasar los principales métodos de una lista
#creamos nuestra lista
numeritos = [10, 20, 30, 40]
print(numeritos)

#append: agrega un elemento al final de la lista
numeritos.append(50)
print(numeritos)

#copy: este método copia una lista pero no la modicia
numeros = numeritos.copy()
print("La lista copiada es: {}".format(numeros))

#extend agrega los elementos de una lista al final de otra lista
numeritos.extend(numeros)
print(numeritos)

#pop: elimina un elemento de la lista, se le pasa la posición de ese elemento (index) y retorna el elemento eliminado.
pop_element= numeritos.pop(2) #eliminará el número 30 de la posición 2
print("se eliminó el elemento: {} de la lista: {}".format(pop_element,numeritos))

#remove: se le pasa un elemento, buscará ese elemento en la lista y si eliminará el primer elemento que se buscó
numeritos.remove(40)
#en nuestra lista tenemos el 40 dos veces, solo eliminará el primero
print("Lista después de eliminar el 40 {}".format(numeritos))

#insert: agrega elementos al índice que le indiquemos de la lista
#también funciona para letras
numeritos.insert(1,-6)
print("Nueva lista: ", numeritos)
numeritos.sort()
print("Lista ordenada menor to mayor: ", numeritos)
numeritos.sort(reverse=True)
print("Lista ordenada de mayor to menor: ", numeritos)

#count: retorna el número de veces que aparece un elemento en la lista3
contar = numeritos.count(20)
print("El número 20 aparece {} vez en la lista".format(contar))
index = numeritos.index(20)
print("La posición de 20 en la lista es: ",index)


