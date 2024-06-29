#Tutorial de como funciona el bucle For en Python------------

#Recorrer listas-----------------------------------------------------------

    #lista declarada en una variable
lista = [1,2,3,4,5,6]
for i in lista:
    print(i)

    #lista en el mismo for
for j in [1,4,6,True,"hola", 44.5]:
    print(j) 


#Diccionarios con For...in-----------------------------------------------------

    #solo imprimir la clave
diccionario = {"ivan":22, "jessica":21, "Josue":25, "itzel":23}
for x in diccionario:
    print(x) #en este ejemplo solo se imprime la clave de nuestro diccionario


    #solo imprimir el valor
diccionario1 = {"ivan":22, "jessica":21, "Josue":25, "itzel":23}
for y in diccionario1:
    print(diccionario1[y]) #en este ejemplo solo se imprime el valor de nuestro diccionario

    #imprimir ambos
diccionario2 = {"ivan":22, "jessica":21, "Josue":25, "itzel":23}

for z in diccionario2:
    print(f"nombre {z} edad: {diccionario[z]}")


#Cadenas con For...in----------------------------------------------------------------------

cadena = "ivan"

for nom in cadena:
    print("hola")



#For in range------------------------------------------------------------------------------------------
#nos va permitir controlar el numero de ciclos dentro del for

n=5
for i in range(n):#Ciclo se repetira 5 veces indicado por n
    print("hola")

