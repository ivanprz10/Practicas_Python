#crea un programa en python que reciba 2 enteros introducidos por teclado y maneje la excepcion
def obtener_entero(n1):
    while True:
        try:
            return int(input(n1))
        except :
            print("Eso no es un número entero válido. Por favor, inténtalo de nuevo.")


print("Introduce dos números enteros.")
num1 = obtener_entero("Primer número: ")
num2 = obtener_entero("Segundo número: ")

print(f"Has introducido los números {num1} y {num2}.")