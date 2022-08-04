sol_usd = 0.26
sol_euro = 0.25

opcion = input("Qué quieres convertir:\n"
               "1: soles -> dolares\n"
               "2: dolares -> soles\n"
               "3: soles -> euros\n"
               "4: euros -> soles\n")

texto = "Introduzca la cantidad en {}:\n"

if opcion=='1' :
    soles = int(input(texto.format("soles")))
    dolares = soles*sol_usd
    print(dolares)

elif opcion=='2':
    dolares = int(input(texto.format("dolares")))
    soles = dolares/sol_usd
    print(soles)

elif opcion=='3':
    soles = int(input("soles"))
    euros = soles*sol_euro
    print(euros)

elif opcion == '4':
    euros = int(input("euros"))
    soles = euros/sol_euro
    print(soles)
else:
    print("Solo tienes que seleccionar 1,2,3 or 4")