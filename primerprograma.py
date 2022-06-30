numero1 = int(input("Introduce el priemer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

print("El número más grande es: {}".format(max((numero1,numero2,numero3))))
print("El número mínimo es: {}".format(min(numero1,numero2,numero3)))

print("#########")
print("El número más grande de {}, {} y {} es: {} y el más pequeño es: {}".format(numero1,numero2,numero3,
                                                                            max(numero1,numero2,numero3),
                                                                            min(numero1,numero2,numero3))
      )