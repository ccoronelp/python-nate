num1 = int(input("Ingrese número: "))
num2 = int(input("Ingrese número: "))


def mayor(n1, n2):
    if n1 > n2:
        print("El mayor es: ",n1)
    elif n1==n2:
        print("Son iguales")
    else:
        print("El mayor es: ",n2)


mayor(num1, num2)