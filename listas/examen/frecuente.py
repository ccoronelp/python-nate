colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']


lista = ['rojo', 'verde', 'rojo', 'rojo', 'azul', 'azul', 'verde', 'verde', 'rojo', 'azul', 'rojo', 'verde', 'rojo', 'rojo', 'verde', 'verde', 'azul', 'verde', 'rojo', 'verde', 'azul', 'verde', 'rojo', 'azul', 'verde', 'rojo', 'verde', 'verde', 'rojo', 'verde', 'azul', 'rojo', 'rojo', 'azul', 'amarillo', 'rojo', 'rojo', 'verde', 'verde']
# color_frecuente(lista) debió entregar "rojo" y 15, pero entregó "verde" y 15 

def color_frecuente(lista):
    cant_azul = 0
    cant_rojo = 0
    cant_verde = 0
    cant_amarillo = 0
    for element in lista: 
        if 'azul' == element:
            cant_azul += 1
        if 'rojo' == element:
            cant_rojo += 1
        if 'verde' == element:
            cant_verde += 1
        if 'amarillo' == element:
            cant_amarillo += 1
    
    elementos = [
        ['azul',cant_azul],
        ['rojo',cant_rojo],
        ['verde',cant_verde],
        ['amarillo',cant_amarillo]
    ]

    mayor = ['',0]
    for colores in elementos:
        if colores[1]>mayor[1]:
            mayor[1] = colores[1]
            mayor[0] = colores[0]
    
    return (mayor[0],mayor[1])

color,valor = color_frecuente(lista)
print(color,valor)