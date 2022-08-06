x = 10
my_name = 'Carlos'
my_fruits = ['apple','pineaple','strawberry','orange']

while x<10:
    print(x)
    x+=1
else:
    print('X no es mayor que 10')


for fruit in my_fruits:
    #no deseo hacer nada
    pass

for letter in my_name:
    if letter == 'a':
        continue
    
    print(letter)

for letter in 'Carlos':
    if letter == 'a':
        break
    print (letter)