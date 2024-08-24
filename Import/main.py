#desde este archivo principal llamado "main.py" llamaremos funciones, variables, listas, tuplas
#Diccionarios, etc desde otros archivos.py 

#FUNCIONES :)

#importamos desde arch_Dest las funciones de saludar y despedir 
from arch_Funciones import saludar, despedir
#mandamos a llamar saludar y despedir de aquel archivo
saludar()
despedir()

#----------------------------------------------------------------------------------------------------------------------------------

#LISTAS

#tambien podemos imprtar el archivo simplemente con el import 
#y al momento de querer llamar estos elementos 
#lo llamaremos con el nombre del archivo seguido de un punto y el nombre del 
#elemento que querramos ejecutar Ejemplo: 
#nombre_archivo.nombreElemento
import arch_Listas

#mandamos a llamar a estos elementos como lo mencionamos antes :)
print(f"esto es una lista: {arch_Listas.lista}")

print(f"esta es una tupla : {arch_Listas.tupla}")



#----------------------------------------------------------------------------------------------------------------------------------

#DICCIONARIOS
#al igual que en el ejemplo anterior cuando no especificamos que elementos se recibiran
#igual podemos importar el archivo pero nombrandolo con un alias, es decir en vez de llamarlo como
#en el ejemplo anterior (nombre_archivo.nombreElemento)
#ahora lo llamaremos 
#alias.nombreElemento
import arch_Diccionario as dic

print(dic.Diccionario[1])
print(dic.Diccionario[2])
print(dic.Diccionario[3])
print(dic.Diccionario[4])
print(dic.Diccionario[5])


print(f"el diccionario completo es : {dic.Diccionario}")





