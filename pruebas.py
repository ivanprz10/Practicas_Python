#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#-------------------------------------------------------------------------------------------------------------
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





















