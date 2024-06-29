#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------

import random

aleatorio = random.randint(1,10)

print(aleatorio)

acierto = True
print("el numero secreto es: ",aleatorio)

while acierto == True:
    n = int(input("ingrese un numero aleatorio entre uno y 10: "))

    if n == aleatorio:
        print("le atinaste, felicidades:)")
        acierto = False
    else:
        print("fallaste, intentalo de nuevo")
