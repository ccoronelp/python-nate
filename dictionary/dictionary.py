my_dictionary = {
	'nombre' : 'Carlos',
	'edad' : 18,
	'listita' : ['platano','manzana','leche']
}
# Agregando otro elemento

my_dictionary['otra-llave'] = 300

print (my_dictionary)

#mostrando las llaves de mi diccionario
print(my_dictionary.keys())

#mostrando los valores de mi diccionario
print(my_dictionary.values())

#mostrando los pares de mi diccionario
print(my_dictionary.items())