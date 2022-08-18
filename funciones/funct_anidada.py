#como es variable global, todas las funciones le pueden llamar

name = 'VARIABLE GLOBAL'

def saludo():
    #enclosing variable: entre dos funciones
    name = 'Jocar'

    def hola():
        #variable local:
        name = 'variable local'
        print('Hola '+name)

    hola()
saludo()

#reasignando variables
x = 50
def imprime():
    #reasignación local
    x = 200
    print(f'fui localmente cambiado de x a {x}')
    #reasignación global
    

def modificandoVarGlobal():
    global x 
    x = 500


imprime()
modificandoVarGlobal()

print('Mi valor global es {}'.format(x))
