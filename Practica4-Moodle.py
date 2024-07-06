#PRACTICA #4 TIPOS DE COLECCION DE DATOS
#-------------------------------------------------------------------------------------------------------------------------
#1.-
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

listaAleatoria=[2,3,5,1,2,8,7,6,4,9]

for i in listaAleatoria:
    cuadrado = i**2
    cubo = i ** 3

    print("valor: ",i,"al cuadrado es:", cuadrado, "al cubo",cubo)


#---------------------------------------------------------------------------------------------------------------------------
#2.-
#Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado.
#Copia los elementos de la lista en otra lista pero en orden inverso,
#y muestra sus elementos por la pantalla
cadenas = []
print("Introduce 5 cadenas de caracteres:")
for i in range(5):
    cadena = input(f"Introduce la cadena {i+1}: ")
    cadenas.append(cadena)

cadenas_invertidas = cadenas[::-1]  # Usamos slicing para invertir la lista

#Mostrar los elementos de la lista invertida
print("\nElementos de la lista invertida:")
for cadena in cadenas_invertidas:
    print(cadena)

#---------------------------------------------------------------------------------------------------------------------------
#3.-