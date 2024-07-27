# Python ofrece una variedad de métodos útiles que puedes utilizar para manipular estas listas.
#  Aquí te explico algunos de los métodos más comunes y 
# útiles que puedes usar para trabajar con listas en Python.



#podemos agregar elementos usando append() extend() insert()---------------------------------------------------------------------------------------------------
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


#count-------------------------------------------------------------------------------------------------------------------------------------------
#Devuelve el número de veces que x aparece en la lista.


numeros = [1, 2, 3, 2, 2, 4]
cuenta = numeros.count(2)
print(cuenta)  # 3


#INDEX---------------------------------------------------------------------------------------------------------------------------------------------
#Devuelve el índice del primer elemento cuyo valor es igual a x.
frutas = ['manzana', 'plátano', 'naranja']
indice = frutas.index('naranja')
print(indice)  # 2





#POP Y REMOVE---------------------------------------------------------------------------------------------------------------------------------------------
#pop:Elimina el elemento en la posición dada en la lista y lo devuelve. 
# Si no se especifica un índice, pop() elimina y devuelve el último elemento de la lista.

#remove: Eliminar la primera ocurrencia de value en la lista.


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


#REVERSE-----------------------------------------------------------------------------------------------------------------------------------------
#Invierte los elementos de la lista en su lugar.
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]


#SORT-----------------------------------------------------------------------------------------------------------------------------------------
#Ordena los elementos de la lista (los elementos son modificados en su lugar).
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]


