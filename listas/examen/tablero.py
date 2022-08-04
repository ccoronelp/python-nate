from grpc import protos_and_services


tablero = [ [' ', 'X', ' ', 'X'],
            ['X', ' ', ' ', ' '],
            [' ', 'X', 'X', ' '],
            ['X', ' ', ' ', 'X']
            ]



def buscaminas(tablero, i, j):
    cantidad = 0
    if 0>i or i>len(tablero):
        return('Error, la coordenada está fuera del rango de la tablero')
    
    if 0>j or j>len(tablero):
        return('Error, la coordenada está fuera del rango de la tablero')

    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if (tablero[x][y] == 'X') and 0<=x<len(tablero) and 0<=y<len(tablero):
                cantidad+=1

    if tablero[i][j]=='X':
        return cantidad-1
    else:
        return cantidad


resultado = buscaminas(tablero,1,1)
print (resultado)