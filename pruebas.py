#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#-------------------------------------------------------------------------------------------------------------
def verificar_rango(num1, num2):
    while not ((1 <= num1 <= 10) and (1 <= num2 <= 10)):
        print("Uno o ambos números están fuera del rango. Inténtelo de nuevo.")
        num1 = int(input("Ingrese el primer número (1-10): "))
        num2 = int(input("Ingrese el segundo número (1-10): "))
    
    print("¡Ambos números están dentro del rango!")

# Ejemplo de uso
num1_inicial = int(input("Ingrese el primer número (1-10): "))
num2_inicial = int(input("Ingrese el segundo número (1-10): "))

verificar_rango(num1_inicial, num2_inicial)

















