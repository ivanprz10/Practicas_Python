import random
from diagramas import diagramasAhorcado
from palabra import palabras


palabraAdivinar = random.choice(palabras)

guiones=["-"] * len(palabraAdivinar)

vidas= 7

erradas =[]

while vidas > 0 and "-" in guiones:
    letra = input("ingresa una letra: ").lower()

    if letra in palabraAdivinar: 
        for i in  range(len(palabraAdivinar)):
            if palabraAdivinar [i] == letra:
                guiones[i] = letra
    else:
        erradas.append(letra)
        print("esa letra no existe en la palabra :(")
        print(f"letras erradas {erradas}\n")
        
        vidas -=1
        print(diagramasAhorcado[vidas])
        print(f"vidas restantes = {vidas}")
    print(guiones)
if "-" in guiones:
    print(guiones)
else: 
    print(f"FELICIDADES, HAS GANADO EL JUEGO :)")    