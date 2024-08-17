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


#----------------------------------------METODOS DE LOS DICCIONARIOS------------------------------------------------

#get()--------------------------------------------------------------------
#es un método utilizado en diccionarios en Python para acceder al valor asociado con una clave k. 
# Si la clave k no existe en el diccionario, en lugar de arrojar un error, 
# el método devuelve un valor por defecto d si se proporciona, o None si no se especifica.


# Crear un diccionario de ejemplo
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Usando get() para obtener el valor de la clave 'b'
valor = mi_diccionario.get('b')
print(valor)  # Salida: 2

# Usando get() para una clave que no existe en el diccionario
valor = mi_diccionario.get('d')
print(valor)  # Salida: None

# Usando get() con un valor por defecto para una clave que no existe
valor = mi_diccionario.get('d', 0)
print(valor)  # Salida: 0




#items()------------------------------------------------------------------------------------
#se usa para devolver una vista de todos los pares clave-valor (items) en un diccionario . 
# El resultado es un objeto de vista que contiene los elementos del diccionario como tuplas de la forma 
# (clave, valor).

# Crear un diccionario de ejemplo
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener los pares clave-valor del diccionario
items = mi_diccionario.items()

# Mostrar los items
print(items)  # Salida: dict_items([('a', 1), ('b', 2), ('c', 3)])

# Convertir los items a una lista de tuplas
items_lista = list(items)
print(items_lista)  # Salida: [('a', 1), ('b', 2), ('c', 3)]

# Iterar sobre los items del diccionario
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")



