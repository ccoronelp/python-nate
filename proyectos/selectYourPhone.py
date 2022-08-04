#Este programa nos ayudará a elegir un teléfono = )

mensaje = "WELCOME TO PHONE SELECTOR"
mensaje2 = "EL CELULAR PERFECTO PARA TI ES:\n"
print(mensaje+"\n"+len(mensaje)*"-")

os = input("Escribe\n 1-Para iPhone\n 2-Para Android\n")
if os == '1':
    you_have_money = input("Tienes dinero?\n S - Sí\n N - No\n")
    if you_have_money == 'S':
        print(mensaje2 + len(mensaje) * "-" + "\n # iPhone ultra pro max")
    else:
        print(mensaje2 + len(mensaje) * "-" + "\n # iPhone segunda mano")

elif os == '2':
    you_have_money = input("Tienes dinero?\n S - Sí\n N - No\n")
    if you_have_money == 'N':
        print(mensaje2+len(mensaje)*"-"+"\n # Android chino 100 soles")
    else:
        camara = input("Te importa la cámara?\n S - Sí\n N - No\n ")
        if camara == 'S':
            print(mensaje2 + len(mensaje) * "-" + "\n # Google pixel super cámara")
        else:
            print(mensaje2 + len(mensaje) * "-" + "\n # Android calidad precio")
