# Programa preguntará al jugador si un número y le dirá si ganó
import random
n_win = random.randint(0,10)

n_player = int(input("Escribe tu número ganador del 0-10: "))
if n_player>10 or n_player<0:
    print("Alerta: solo tienes que ingresar números entre 0 y 10")
elif n_win==n_player:
    print("Felicidades jugador, has ganado")
else:
    print("Perdiste, sigue intentando")