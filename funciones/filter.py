
numbers = [1,2,3,4,5,6]

def check_par(num):
    return num%2 == 0

for n in filter(check_par,numbers):
    print (n)