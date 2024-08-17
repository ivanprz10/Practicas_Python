#GENERADORES

lim = int(input("ingrese un limite de multiplos de 5: "))
numero = 1
mul = []
while numero <=lim:
    mul.append(numero * 5)
    numero = numero + 1 

for i in mul:
    print(i)


#---------------------------------------------------
def multiplos(lim):
    lista = []
    numero= 1
    while numero <=lim:
        lista.append(numero*5)
        numero = numero+1
    return lista


var = int(input("ingresa un valor limite para ser multiplo de 5"))

lis = multiplos(var)

print(lis)

#-------------------------------------------------------------------------------

def mul(lim):
    numero=1
    while numero<=lim:
        yield numero * 5
        numero = numero + 1


var = int(input("ingresa un valor limite para ser multiplo de 5: "))
gen = mul(var)

print(next(gen))
print(next(gen))
print(next(gen))


