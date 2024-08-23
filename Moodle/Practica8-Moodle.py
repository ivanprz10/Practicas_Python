#Escribe un programa Python que pida un número por teclado 
#y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado,
#y los valores sean los cuadrados de las claves.

# Pedir al usuario que ingrese un número
n = int(input("Introduce un número: "))

# Crear un diccionario con las claves desde 1 hasta n y los valores como el cuadrado de las claves
diccionario = {i: i**2 for i in range(1, n+1)}

# Mostrar el diccionario
print(diccionario)

#o--------------------------------

# Pedir al usuario que introduzca un número y convertirlo a entero
numero = int(input("Dime un número: ")) 

# Inicializar un diccionario vacío donde se almacenarán los números y sus cuadrados
cuadrados = {} 

# Bucle que va desde 1 hasta el número introducido (inclusive)
for num in range(1, numero + 1): 
    # Calcular el cuadrado del número actual y guardarlo en el diccionario
    cuadrados[num] = num ** 2 

# Bucle para recorrer cada par clave-valor en el diccionario
for num, valor in cuadrados.items(): 
    # Imprimir la clave (número) y su valor (cuadrado) en el formato "clave -> valor"
    print(f"{num}-->{valor}")

#------------------------------------------------------------------------------------------------------------------------------------

# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena. 
# Solicita al usuario que introduzca una cadena de texto
cadena = input("Introduce una cadena: ")

# Inicializa un diccionario vacío para almacenar las apariciones de los caracteres
apariciones = {}

# Recorre cada carácter en la cadena
for i in cadena:
    # Si el carácter ya está en el diccionario, incrementa su contador
    if i in apariciones:
        apariciones[i] += 1
    # Si el carácter no está en el diccionario, se añade con un contador de 1
    else:
        apariciones[i] = 1

# Muestra el diccionario resultante
print("Las apariciones de cada carácter son:")
print(apariciones)


#----------------------------------------------------------------------------------------------------------------------------------------

#Vamos a crear un programa en Python donde vamos a declarar un diccionario 
# para guardar los precios de las distintas frutas. El programa pedirá el nombre de la fruta 
# y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados 
# en el diccionario. Si la fruta no existe nos dará un error. 
# Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.

# Declaramos el diccionario con los precios de las frutas
precios_frutas = {
    "manzana": 3.50,
    "naranja": 2.00,
    "plátano": 1.50,
    "pera": 4.00,
    "uva": 5.00
}

while True:
    # Solicita el nombre de la fruta al usuario
    fruta = input("Introduce el nombre de la fruta que se ha vendido: ").lower()

    # Verifica si la fruta existe en el diccionario
    if fruta in precios_frutas:
        # Solicita la cantidad vendida
        cantidad = float(input("Introduce la cantidad vendida (en kg): "))

        # Calcula el precio final
        precio_final = precios_frutas[fruta] * cantidad

        # Muestra el precio final
        print(f"El precio final de {cantidad} kg de {fruta} es: ${precio_final}")
    else:
        # Muestra un mensaje de error si la fruta no existe en el diccionario
        print("Error: La fruta no está en el diccionario.")

    # Pregunta si desea realizar otra consulta
    otra_consulta = input("¿Quieres hacer otra consulta? (si/no): ").lower()
    
    # Si la respuesta es no, termina el bucle
    if otra_consulta != "si":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break

