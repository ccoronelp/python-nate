

list_nums = [8.5,7.0,9.5,8.0,9.0,8.8,7.5,10]

lista = [18, 92, 35, 100, 57, 30, 45, 32, 64, 62, 2, 53, 8]
# promedio_std(lista) debió entregar 46.0 y 28.447, pero entregó 46.0 y 29.609 


def promedio_std(lista):
    x = 0
    y = 0
    suma = 0
    #sacando promedio
    for num in lista:
        suma += num
    
    x = suma/len(lista)
    #sacando desviacion 
    suma2 = 0
    for num in lista:
        #sacando suma desviaciones al cuadrado 
        suma2 += (num-x)**2
    
    # calculando la desviación estándar
    y = ((suma2/(len(lista)))**(0.5))

    return (x,y)

promedio,desviacion = promedio_std(lista)
print(promedio,desviacion)