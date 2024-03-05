import random
import sys

usuario = sys.argv[1]

eleccion = ["piedra", "papel", "tijera"]

npc = random.choice(eleccion)
print(f"tu jugaste {usuario} ")

if usuario not in eleccion:
        print("argumento invalido: debe ingresar piedra, papel o tijera")
        sys.exit(1)
        
print(f"computadora jugo {npc} ")

if usuario == npc:
    print("Esto es un EMPATE!!!")

elif ((usuario == "piedra" and npc == "tijera") or
    (usuario == "tijera" and npc == "papel") or
    (usuario == "papel" and npc == "piedra")):
    print("GANASTE!!!")    

else :
    print("PERDISTE")

