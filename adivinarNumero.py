#adivinar un numero del rango del uno al 10 
import random

aleatorio = random.randint(1,10)

# print("numero secreto es: ",aleatorio)

condicion = True

while condicion == True:
    numero = int(input("ingresa tu numero: "))

    if numero == aleatorio:
        print("FELICIDADES \nhas ganado")
        condicion = False
    else:
        print("intentalo de nuevo ")

