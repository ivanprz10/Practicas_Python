#La función filter() en Python se usa para filtrar elementos de una secuencia 
# (como una lista o tupla) en función de una función que devuelve True o False. 
# Solo los elementos para los que la función devuelve True son incluidos en el resultado.
#Sintaxis
#filter(función, secuencia)

#ejemplo filtrar valores positivos
def funcion(lista):
    return lista>=0#retorna un verdadero si es que es True

lista=[1,2,-1,-2,2,4,5,6,-5]#lista con elementos positivos y negativos

fil = list(filter(funcion,lista))#funcion filter 
print(fil)#imprimiendo

#------------------------------------------------------------------------------------------------------------------------------
#filtrar si es par
def es_par(x):
    return x % 2 == 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Aplicar filter
resultado = filter(es_par, numeros)

# Convertir a lista
print(list(resultado))  # Salida: [2, 4, 6, 8, 10]



#---------------------------------------------------------------------------------------------------------------------
#Ejemplo con Lambda

lista=[1,2,-1,-2,2,4,5,6,-5]

#Declaramos la funcion Lambda
var = list(filter(lambda lis:lis>=0,lista))

print(var)