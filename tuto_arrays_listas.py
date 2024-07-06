#La fabricacion de un array o lista conlleva la siguiente sintaxis

array = [2,4,5,7,9,10]#estamos creando una lista con 6 valores de tipo entero
#para esto hay que recordar que la primera posicion es cero y para la ultima podemos usar -1

print(array[0])#indicamos que nos muestre el array en su posicion 0


#----------------------------------------------------------------------------------------------------------------------
#podemos modificar los valores de las listas con el indice especifico: (ejemplo)
lista = [10, 20, 30]
lista[1] = 200
print(lista)  # Salida: [10, 200, 30]

#---------------------------------------------------------------------------------------------------------------------
#podemos agregar elementos usando append() extend() insert()
lista = [1, 2, 3]

# Agregar un solo elemento
lista.append(4)
print(lista)  # Salida: [1, 2, 3, 4]

# Agregar múltiples elementos
lista.extend([5, 6])
print(lista)  # Salida: [1, 2, 3, 4, 5, 6]

# Insertar un elemento en una posición específica
lista.insert(2, 'nuevo')
print(lista)  # Salida: [1, 2, 'nuevo', 3, 4, 5, 6]



#------------------------------------------------------------------------------------------------------------------------
#podemos eliminar elementos usando remove () pop() del
lista = [1, 2, 3, 4, 5]

# Eliminar un elemento por valor
lista.remove(3)
print(lista)  # Salida: [1, 2, 4, 5]

# Eliminar un elemento por índice
lista.pop(1)
print(lista)  # Salida: [1, 4, 5]

# Eliminar un elemento por índice usando 'del'
del lista[0]
print(lista)  # Salida: [4, 5]


#----------------------------------------------------------------------------------------------------------------------
#slicing para obtener sublistas

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Obtener elementos desde el índice 2 al 5
sublista = lista[2:6]
print(sublista)  # Salida: [3, 4, 5, 6]

# Obtener elementos desde el inicio hasta el índice 3
sublista = lista[:4]
print(sublista)  # Salida: [1, 2, 3, 4]

# Obtener elementos desde el índice 5 hasta el final
sublista = lista[5:]
print(sublista)  # Salida: [6, 7, 8, 9, 10]


#------------------------------------------------------------------------------------------------------------------------
#podemos obtener la longitud de la lista con len()
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print(longitud)  # Salida: 5


#------------------------------------------------------------------------------------------------------------------------
#agregar valores a la lista leidos por teclado

lista =[]
print("hola ingrese la cantidad de valores que tendra su lista: ")
rango=int(input())
for i in range(rango):
    valor = input(f"introduzca el valor ({i+1})")
    lista.append(valor)
print(lista)

#------------------------------------------------------------------------------------------------------------------------
#sumar el contenido de una lista
lista10=[1,2,3,4,5]
suma = sum(lista10)
print(suma)

#sacar el valor maximo de una lista
lista11=[1,2,10,4,5]
valMax = max(lista10)
print(valMax)

#sacar el valor minimo de una lista
lista10=[1,2,10,4,5]
valMin = min(lista10)
print(valMin)

#sacar la media de una lista
lista10=[1,2,3,4,5]
media = sum(lista10) / len(lista10)
print(media)


