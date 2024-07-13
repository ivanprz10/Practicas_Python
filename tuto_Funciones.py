#TUTORIAL DE COMO USAR LAS FUNCIONES EN PYTHON, ESTAS NOS SIRVEN YA QUE ES UN FRAGMENTO DE CODIGO
#QUE PUEDE DEVOLVER UN VALOR, E INCLUSO REPERTIR UN FRAGMENTO DE CODIGO DE UNA MANERA EFICIENTE

#PRIMERA FUNCION BASICA--------------------------------------------------------------------------------------

def saludar():#Declaramos una funcion llamada saludar seguida de 2 parentesis donde iran parametros, 
              #seguido de dos puntos
    print("¡¡Hola!!")#imprimimos un mensaje saludando

saludar()#mandamos a llamar a nuestra funcion

#PARAMETROS Y ARGUMENTOS-------------------------------------------------------------------------------------

def suma(n1,n2):#funcion que recibe como parametros 2 variables 
    print(n1)
    print(n2)

suma(5,6)#mandamos a llamar a nuestra funcion asi como enviamos 2 argumentos

#NONETYPE----------------------------------------------------------------------------------------------------

def sindato(nombre):#funcion declarada con un parametro
    print(nombre)#imprimimos un parametro

dato=sindato("juan")#igualamos la funcion a una variable
print(dato)#imprimimos esta variable pero de salida tenderia : None (Nonetype)

#RETURN-----------------------------------------------------------------------------------------------------------------
#return nos sirve para retornar un valor que nuestra funcion en especifico realice

def suma(num1,num2):
    res=num1+num2
    return res

n1=2
n2=3
sum=suma(n1,n2)
print(sum)

