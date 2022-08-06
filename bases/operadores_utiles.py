from random import shuffle,randint

#range
for num in range(10):
    print (num)

for num in range(4,20,2):
    print (num)

my_list = list(range(4,20,2))
print ('my list:',my_list)

#enumerate()

my_lastName = 'Coronel'

#la forma normal de recorrerlo sería:
for index,letter in enumerate(my_lastName):
    print('my index is {} and my letter is {}'.format(index,letter))

#••• zip()
list_num = [1,2,3]
list_letters = ['a','b','c']
list = [200,300,400]
dictionary = {
    'uno' : 1,
    'dos' : 2,
    'tres' : 3
}

new_list = zip(list_num,list_letters,list)

for element in new_list:
    print(element)

#buscando en diccionario
if 1 in dictionary.values():
    print('Si se encuentra el elemento')

#buscando en listas
if 1 in list:
    print('si se encuentra el elemento')

max_list_num = max(list_num)
min_list_num = min(list_num)
max_list_letter = max(list_letters)
min_list_letter = min(list_letters)

print('Número máximo: {}, número mínimo: {}'.format(max_list_num,min_list_num))
print('Letra máxima: {}, letra mínima: {}'.format(max_list_letter,min_list_letter))

#función shuffle() para aleatorizar los elementos
list_shuffle = shuffle(my_list)
print('Shuffle: ',my_list)

#randint() para elegir un número entero de un rago de números
number = randint(1,100)
print(number)

