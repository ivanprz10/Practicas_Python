#PRACTICA #4 TIPOS DE COLECCION DE DATOS
#-------------------------------------------------------------------------------------------------------------------------
#1.-
#Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
#y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.

listaAleatoria=[2,3,5,1,2,8,7,6,4,9]

for i in listaAleatoria:
    cuadrado = i**2
    cubo = i ** 3

    print("valor: ",i,"al cuadrado es:", cuadrado, "al cubo",cubo)


#---------------------------------------------------------------------------------------------------------------------------
#2.-
#Crea una lista e inicializarla con 5 cadenas de caracteres leídas por teclado.
#Copia los elementos de la lista en otra lista pero en orden inverso,
#y muestra sus elementos por la pantalla
cadenas = []
print("Introduce 5 cadenas de caracteres:")
for i in range(5):
    cadena = input(f"Introduce la cadena {i+1}: ")
    cadenas.append(cadena)

cadenas_invertidas = cadenas[::-1]  # Usamos slicing para invertir la lista

#Mostrar los elementos de la lista invertida
print("\nElementos de la lista invertida:")
for cadena in cadenas_invertidas:
    print(cadena)

#---------------------------------------------------------------------------------------------------------------------------
#3.- Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno 
# (comprendidas entre 0 y 10).
#  A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor.

calificaciones = []
print("ingrese las calificaciones del alumnos de los 5 modulos cursados")

for i in range (5):
    cal = float(input(f"ingrese la calificacion del modulo({i+1}): "))
    calificaciones.append(cal)

print(f"las calificaciones almacenadas son {calificaciones}")

media = sum(calificaciones) / len(calificaciones)
print(f"la media de su calificacion es: {media}")

calMax = max(calificaciones)
print(f"la calificacion mas alta es: {calMax}")

calMin =min(calificaciones)
print(f"la calificacion mas baja es: {calMin}")


#---------------------------------------------------------------------------------------------------------------------------
#4.-
#Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase 
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
# Guarda la información en un diccionario cuya claves serán los nombres de los alumnos 
# y los valores serán listados con las notas de cada alumno.

#El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas 
# hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos 
# y la nota media obtenida por cada uno de ellos. Nota: 
# si se introduce el nombre de un alumno que ya existe el programa nos dará un error.

alumnos = {}  # Diccionario para almacenar los datos de los alumnos

    # Solicitar el número de alumnos a introducir
num_alumnos = int(input("¿Cuántos alumnos vas a introducir? "))

for i in range(num_alumnos):
        while True:
            nombre = input("Introduce el nombre del alumno: ")
            if nombre in alumnos:
                print("Error: Ya existe un alumno con ese nombre. Introduce un nombre diferente.")
            else:
                break

        # Lista para guardar las notas del alumno
        notas = []
        print(f"Introduce las notas de {nombre} (introduce un número negativo para terminar):")

        while True:
            nota = float(input("Nota: "))
            if nota < 0:
                break
            notas.append(nota)

        # Almacenar las notas en el diccionario con el nombre del alumno como clave
        alumnos[nombre] = notas

# Mostrar la lista de alumnos y la nota media obtenida por cada uno
print("\nLista de alumnos y sus notas medias:")
for nombre, notas in alumnos.items():
        media = sum(notas) / len(notas) if notas else 0
        print(f"{nombre}: Nota media = {media:.2f}")


#---------------------------------------------------------------------------------------------------------------------------
#5.- Crea una tupla con los meses del año, pide números al usuario,
#  si el número está entre 1 y la longitud máxima de la tupla,
#  muestra el contenido de esa posición sino muestra un mensaje de error.
#  El programa termina cuando el usuario introduce un cero.

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    
print("Introduce un número entre 1 y 12 para elegir un mes (0 para terminar):")

while True:
        
    numero = int(input("Número del mes: "))
    if numero == 0:
        print("Programa terminado.")
        break
    elif 1 <= numero <= 12:
        print(f"El mes seleccionado es: {meses[numero - 1]}")
    else:
        print("Error: Por favor introduce un número válido entre 1 y 12.")

