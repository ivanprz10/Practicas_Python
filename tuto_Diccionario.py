#Para crear un diccionario es necesario contar con 2 concepto
#KEY : VALUE


diccionario = {
    5 : "valor1",
    2 : "valor2",
    3 : "valor3"
}
print(diccionario[5])



#-------------------------------------------------------------------------------------------------------
#ingresar valores por teclado ejemplo
# Iniciar un diccionario vacío
diccionario = {}

print("Introduce datos en el diccionario. Escribe 'fin' como nombre para terminar.")

# Bucle para introducir datos
while True:
    # Solicitar al usuario que introduzca un nombre
    nombre = input("Introduce el nombre: ")
    if nombre == 'fin':
        break  # Si el nombre es 'fin', salir del bucle

    # Solicitar al usuario que introduzca la edad
    edad = input(f"Introduce la edad de {nombre}: ")

    # Añadir el par nombre-edad al diccionario
    diccionario[nombre] = edad

# Mostrar el diccionario completo
print("\nDiccionario final:")
for nombre, edad in diccionario.items():
    print(f"{nombre}: {edad}")
