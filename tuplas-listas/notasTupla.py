#1.	Crear una tupla para almacenar las notas de matemática, comunicación y computación.
tupla = ()
for nota in range(3):
    curso = input("Ingresa nombre curso: ")
    nota = input("Ingrese nota: ")
    tupla_a = (curso, nota)
    tupla += tupla_a

print(tupla)