#La función reduce() en Python se usa para aplicar una función acumulativa a los elementos de una secuencia, 
# reduciendo la secuencia a un solo valor. Esta función se encuentra en el módulo functools.

#Sintaxis

#reduce(función, secuencia)



from functools import reduce

def  reducir(x,y):
    return (x+y)

lista=[1,2,3,4,5]

var = reduce(reducir,lista)
print(var)



#---------------------------------------------------------------------------------------------------------------------
#Ejemplo con Lambda

lista=[1,2,3,4,5]

var = reduce(lambda x,y:x+y, lista)

print(var)


