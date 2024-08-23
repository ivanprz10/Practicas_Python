#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#-------------------------------------------------------------------------------------------------------------

import random
print("Este programa te pregunta multiplicaciones al azar")
multi=lambda x, y: x*y
i=True
while i==True:
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    var1=float(input(f"¿Cuánto es {num1}*{num2}: "))
    num1=multi(num1, num2)
    if var1==num1:
        print("**** Respuesta correcta ****")
    else:
        print("**** Respuesta Incorrecta ****")
        print(f"El resultado correcto es {num1}")


































