#Recorriendo lista

list_mumbers = [20,15,5,6,9,7,6,10]

list_letters_num = [
    ['uno',1],
    ['dos',2],
    ['tres',3]
]

tuple_letters_num = [
    ('uno',1),
    ('dos',2),
    ('tres',3)
]

my_dict = {
    'nombre' : 'Carlos',
    'edad' : 31,
    'nacimiento': 1991
}

for num in list_mumbers:
    print (num)


#for num,letter in list_mumbers:
    #print (num,letter)#no se puede desenpaquetar una lista de listas

#con índice 

for indice in range(2,10,2):
    print (indice)

for letter,num in tuple_letters_num:
    print(letter,num)

#recorriendo un dictionary, imprime solo las llaves
for dict in my_dict:
    print(dict)

#si deseamos que imprima solo los datos usamos la función .values()
for values in my_dict.values():
    print(values)

#podemos desempaquetar the dictionary too
for key,value in my_dict.items():
    print('My key is: {} and my value is: {}'.format(key,value))