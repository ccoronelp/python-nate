#se harán preguntas y se calculará un valor

titulo = "Bienvenido al test sobre queso"
print("\n"+titulo+"\n"+"="*len(titulo)+"\n")

puntos = 0

while True:
    pregunta1 = int(input(
        """Pregunta A: Qué haces cuando vez un queso
                    1. Lo guardo
                    2. Lo tiro
                    3. Lo como
            """
    ))
    if pregunta1!=1 and pregunta1 != 2 and pregunta1 != 3:
        print("Por favor ingresa un valor entre 1 y 3")
    if pregunta1==1:
        puntos += 5
        break
    if pregunta1==2:
        puntos += 0
        break
    if pregunta1==3:
        puntos += 10
        break



while True:
    pregunta2 = int(input(
        """Pregunta B: ¿Cómo te gusta la hamburguesa?
            1. Sin queso
            2. Con queso
            3. Pan y queso
    """
    ))
    if pregunta2<1 or pregunta2>3:
        print("Por favor ingresa un número entre 1-3")
    if pregunta2 == 1:
        pregunta2 += 0
        break
    if pregunta2 == 2:
        pregunta2 += 10
        break
    if pregunta2 == 3:
        pregunta2 += 5
        break

print("Puntos: ", puntos)