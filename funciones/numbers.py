def sumar(n1,n2):
    return(n1+n2)


#esta función se puede escribir así:
def sumar2(*args):
    return(sum(args))


print (sumar2(20,21))

#cómo manipular los elementos dentro de la función?

def suma3(*args):
    for argumento in args:
        print (argumento)

suma3('hola',3,True)

#usemos **kargs que es para enviar diccionarios

def arg_dic(**kargs):
    if 'nombre' in kargs:
        print('Existe la persona',kargs['nombre'])

arg_dic(nombre='Carlos',apellido='Coronel')