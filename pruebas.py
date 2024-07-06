#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------


    # Tupla con los meses del año
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
        






