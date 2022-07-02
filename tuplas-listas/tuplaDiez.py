#3.	Crea una tupla de 10 números e imprime el mayor y el menor.
tupla = ()

for indice in range(10):
    nota = int(input("Ingresa número de la posición {}: ".format(indice+1)))
    tupla_a = (nota,)
    tupla += tupla_a

print(tupla)

mayor=0
menor=tupla[0]
for indice in range(len(tupla)):
    if mayor<tupla[indice]:
        mayor = tupla[indice]

    if menor>tupla[indice]:
        menor = tupla[indice]

mensaje1 = "Número mayor: "+str(mayor)
mensaje2 = "Número menor: "+str(menor)
print(len(mensaje1)*"#"+"\n"+mensaje1)
print(len(mensaje2)*"#"+"\n"+mensaje2)