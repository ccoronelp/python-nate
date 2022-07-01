empresa = input("Ingrese nombre de la empresa: ")
n_clientes = input("Ingrese número de clientes: ")
clientes = []
while True:
    if not n_clientes.isdigit():
        n_clientes = input("Ingrese número de clientes: ")
    elif int(n_clientes) <= 0 :
        print("Ingrese un número mayor a cero")
    else:
        n_clientes = int(n_clientes)
        break

for cliente in range(n_clientes):
    nombre_cliente = input("Ingrese cliente número {}: ".format(cliente+1))
    clientes.append(nombre_cliente)

for nombre in clientes:
    print("Nombre cliente {}: ".format(nombre))