#2.	De la tupla anterior sacar el promedio de los 3 cursos.
tupla = ()
for nota in range(3):
    curso = input("Ingresa nombre curso: ")
    nota = input("Ingrese nota: ")
    tupla_a = (curso, nota)
    tupla += tupla_a

print(tupla)
suma = 0
for i in range(1,len(tupla),2):
    if 0 != i % 2:
        suma += int(tupla[i])

print("El promedio es: ", suma/3)