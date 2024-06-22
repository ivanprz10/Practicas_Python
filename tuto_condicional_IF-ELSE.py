#El uso de condicionales IF-ELSE
#--------------------------------------------------------------------------------

#SINTAXIS
if condicion:
    # Bloque de código que se ejecuta si la condición es verdadera
    statement1
    statement2
    # Más statements si es necesario
#--------------------------------------------------------------------------------------------------------------------

#Ejemplo simple del IF

x = 10
if x > 5:
    print("x es mayor que 5")#evaluamos si la variable "x" que equivale a 10 es mayor que 5
    #como la condicion se cumple es decir es verdadera, se ejecuta lo que esta dentro de IF

#--------------------------------------------------------------------------------------------------------------------

# if con else
x = 3
if x > 5:#evaluamos si la condicion se cumple es decir 3 es mayor que 5, en este caso no se cumple, por lo que buscara un else 
    print("x es mayor que 5")
else: 
    print("x no es mayor que 5")


#--------------------------------------------------------------------------------------------------------------------

#if con elif y else
x = 10
if x > 15:
    print("x es mayor que 15")
elif x > 5: #elif es el equivalente a "else if" de otros lenguajes nos sirve para  evaluar múltiples condiciones
    print("x es mayor que 5 pero menor o igual que 15")
else:
    print("x es menor o igual que 5")
