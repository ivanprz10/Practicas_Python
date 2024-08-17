#Los decoradores son un patrón de diseño de software que alteran
#dinámicamente y agregan funcionalidades adicionales a los métodos, funciones
#o clases de Python sin tener que usar subclases o cambiar el código fuente
#decorada.




def decorador(func):  
    # Definimos el decorador, que es una función que toma otra función como argumento.
    def envoltura():  
        # Definimos una función interna llamada 'envoltura', que envuelve la función original.
        print("Algo que se ejecuta antes de la función")
        # Este código se ejecutará antes de la función original.
        func()  
        # Aquí se llama a la función original.
        print("Algo que se ejecuta después de la función")
        # Este código se ejecutará después de la función original.
    return envoltura  
    # El decorador retorna la función 'envoltura' en lugar de la función original.

@decorador  
# Aplicamos el decorador a la función 'saludar'. Es equivalente a 'saludar = decorador(saludar)'.
def saludar():  
    # Definimos la función 'saludar', que será decorada.
    print("¡Hola!")  
    # La función original imprime "¡Hola!".

saludar()  
# Llamamos a la función 'saludar', que ahora está envuelta por la lógica del decorador.

