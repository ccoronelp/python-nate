#8.	Crear una función que reciba como parámetro 2 años e imprimir la diferencia de años.

def diferencia(year1,year2):
    if year1 == year2:
        print("La diferencia es 0")
    elif year1>year2:
        print("La diferencia es: ", year1-year2)
    else:
        print("La diferencia es: ", year2-year1)


diferencia(1999,2022)