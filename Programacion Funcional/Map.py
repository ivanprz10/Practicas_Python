#Esta función trabaja de una forma muy similar a filter(), con la diferencia que en
#lugar de aplicar una condición a un elemento de una lista o secuencia, aplica
#una función sobre todos los elementos y como resultado se devuelve un iterable
#de tipo map:

#Sintaxis de map
#map(función, secuencia)



#funcion que suma un mas dos a cada elemento de la lista iterable

def masdos(lista):

    return lista+2

lista=list(range(1,11))

var = map(masdos,lista)

print(list(var))

#---------------------------------------------------------------------------------------------------------------------

def duplicar(x):
    return x * 2

numeros = [1, 2, 3, 4, 5]

# Aplicar map
resultado = map(duplicar, numeros)

# Convertir a lista
print(list(resultado))  # Salida: [2, 4, 6, 8, 10]


#---------------------------------------------------------------------------------------------------------------------
#Ejemplo con Lambda

numeros = [1, 2, 3, 4, 5]

var = map(lambda x:x**2,numeros)

print(list(var))



