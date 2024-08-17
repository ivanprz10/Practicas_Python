# 1.-Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta 
# que seleccionamos la opción de "Salir". 

while True:
    # mostrar menu
    print("Menú de recomendaciones")
    print(" 1. Literatura")
    print(" 2. Cine")
    print(" 3. Música")
    print(" 4. Videojuegos")
    print(" 5. Salir")
    
    # ingresar una opcion
    opcion = int(input("Elija una opción (1-5): "))
    
    # procesar esa opción
    if opcion == 1:
        print("Lecturas recomendables:")
        print(" + Esperándolo a Tito y otros cuentos de fútbol (Eduardo Sacheri)")
        print(" + El juego de Ender (Orson Scott Card)")
        print(" + El sueño de los héroes (Adolfo Bioy Casares)")
    elif opcion == 2:
        print("Películas recomendables:")
        print(" + Matrix (1999)")
        print(" + El último samurái (2003)")
        print(" + Cars (2006)")
    elif opcion == 3:
        print("Discos recomendables:")
        print(" + Despedazado por mil partes (La Renga, 1996)")
        print(" + Búfalo (La Mississippi, 2008)")
        print(" + Gaia (Mago de Oz, 2003)")
    elif opcion == 4:
        print("Videojuegos clásicos recomendables:")
        print(" + Día del tentáculo (LucasArts, 1993)")
        print(" + Terminal Velocity (Terminal Reality/3D Realms, 1995)")
        print(" + Death Rally (Remedy/Apogee, 1996)")
    elif opcion == 5:
        print("Gracias, vuelva pronto")
        break
    else:
        print("Opción no válida, por favor elija una opción del 1 al 5.")




#--------------------------------------------------------------------------------------------------------------------------
#2.-Mostrar en pantalla los N primero número primos.
#  Se pide por teclado la cantidad de números primos que queremos mostrar. 
import math

while True:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if cant_a_mostrar > 0:
        break

print("1 : 2")  # el primer primo es 2, los otros son todos impares...
cant_mostrados = 1
num = 3  # ...a partir de 3

while cant_mostrados < cant_a_mostrar:
    es_primo = True  # pienso que es primo hasta que encuentre con qué dividirlo
    for divisor in range(3, int(math.sqrt(num)) + 1, 2):  # ya sabemos que es impar
        if num % divisor == 0:  # si la división es exacta...
            es_primo = False  # ...ya no es primo
            break  # salir del bucle si encontramos un divisor
    if es_primo:
        cant_mostrados += 1
        print(cant_mostrados, ": ", num)
    num += 2





#o....


import math

# Solicitar al usuario la cantidad de números primos a mostrar
while True:
    cant_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if cant_a_mostrar > 0:
        break

# Inicializar el contador y el primer número primo
cant_mostrados = 0
num = 2

# Encontrar y mostrar los N primeros números primos
while cant_mostrados < cant_a_mostrar:
    es_primo = True
    if num > 1:
        if num == 2:
            es_primo = True
        elif num % 2 == 0:
            es_primo = False
        else:
            for divisor in range(3, int(math.sqrt(num)) + 1, 2):
                if num % divisor == 0:
                    es_primo = False
                    break
    else:
        es_primo = False

    if es_primo:
        cant_mostrados += 1
        print(f"{cant_mostrados}: {num}")
    num += 1



#--------------------------------------------------------------------------------------------------------------------------
#3.-Una persona adquirió un producto para pagar en 20 meses.
# El primer mes pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. 
# Realizar un algoritmo para determinar cuánto debe pagar mensualmente 
# y el total de lo que pagó después de los 20 meses. 
pago_acum = 0 
pago = 10 
for mes in range(1, 21): 
    pago_acum = pago_acum + pago 
    pago = pago * 2 
print("Al final de los 20 meses tuvo que pagar: ",pago_acum)



#--------------------------------------------------------------------------------------------------------------------------
#4.-Crea una aplicación que pida un número y calcule su factorial 
# (El factorial de un número es el producto de todos los enteros entre 1 y el propio número 
# y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120). 
resultado = 1; 
num=int(input("Dime un número:")) 
for contador in range(2, num+1): 
    resultado = resultado * contador; 
print("El resultado es", resultado)




