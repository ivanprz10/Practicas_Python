def cuadrado(val):
    return val**2

def cubo(val):
    return val*2


valor=int(input("ingrese valor: "))

print(f"el valor al cuadrado es: {cuadrado(valor)}")

print(f"el valor al cubo es: {cubo(cuadrado(valor))}")