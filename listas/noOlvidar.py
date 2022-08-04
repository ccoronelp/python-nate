no_olvidar = ['huevos','queso','lechuga','naranjas',7000]
#para acceder a un elemeno de una lista solo basta con colocar su índice
print (no_olvidar[1])

#También podemos acceder a un corte (slice) de la lista 
print (no_olvidar[1:4])
#lista[inicio:fin:step] 
#step permite difinir cada cuánto puede salatar la lista, por defecto es de 1 en 1
print(no_olvidar[0:4:2])

#imprimir todos los elementos con el elemento for
for notas in no_olvidar:
    print (notas)

##### modificando listas
#concatenar listas
lista2 = ['apio','tomates']
lista3 = no_olvidar+lista2
lista3 = lista2*2

#agregar elementos a la lista -> append
no_olvidar.append('apio')
print(no_olvidar)

#método extend agrega los elementos de una lista a otra lista
no_olvidar.extend(lista2)
print(no_olvidar)

#método insert agrega un elemento en la posición indicada
no_olvidar.insert(2,5000)
print(no_olvidar)

#eliminar un elemento y retornar el elemento eliminado método pop()
#también podemos indicarle un índice para decirle cuál elemento queremos eliminar
elemento_eliminado = no_olvidar.pop()
print('Elemento eliminado: ',elemento_eliminado)
print('Nueva lista: \n',no_olvidar)

#eliminar elementos indicando su índice método remove()
elemento_eliminado = no_olvidar.remove('apio')
print(no_olvidar)

#cantidad de elementos de ua lista len()
print (len(no_olvidar))

#ver si un elemento está en la lista con el operador in
elem_buscar = 'apio'
if elem_buscar in no_olvidar:
    print('Sí {} está en la lista, en la posición {}'.format(elem_buscar,no_olvidar.index(elem_buscar)))
else:
    print('no está en la lista')

#convertir un string separado por comas a lista
#split permite separar elementos según el separador que le indiquemos
lista_string = 'carro, moto, bici, avion'
print (lista_string)
lista_lista = lista_string.split(',')
print (lista_lista)

#ordenar una lista con sort() de menor a mayor
lista_lista.sort()
print(lista_lista)

datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print (trozo)

unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2:3] + unidades[3:7:3] + unidades[7:8]
print (muestra)

def ganador(votos):
  mayor = votos[0]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor

resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]
mayoria = ganador(resultados)

print (mayoria)

tablero = [ [1,2,3], [4,5,6], [7,8,9] ]

for j in range(3):
  for i in range(3):
    print(tablero[j][i],end=" ")


contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print (splitted)