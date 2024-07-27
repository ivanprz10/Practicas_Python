#Este tema abarca todas las funciones y procedimientos específicos que se pueden aplicar a las cadenas (strings)
#  en Python para manipularlas, consultar información sobre ellas, y modificar su contenido.


#COUNT-------------------------------------------------------------------------------------------------------------
#Devuelve el número de veces que se encuentra sub en la cadena. Los
#parámetros opcionales start y end definen una subcadena en la que buscar.

texto = "hola mundo, hola a todos, hola universo"

# Contar cuántas veces aparece la palabra 'hola'
conteo = texto.count("hola")
print(conteo)  # Salida: 3

# Contar cuántas veces aparece 'hola' a partir del índice 10
conteo_desde = texto.count("hola", 10)
print(conteo_desde)  # Salida: 2

# Contar cuántas veces aparece 'hola' entre los índices 10 y 30
conteo_rango = texto.count("hola", 10, 30)
print(conteo_rango)  # Salida: 1



#FIND-------------------------------------------------------------------------------------------------------------
#Devuelve la posición en la que se encontró por primera vez sub en la cadena o
#-1 si no se encontró


texto = "Hola mundo, bienvenido al mundo de Python."

# Buscar una subcadena en el texto
indice = texto.find("mundo")
print(indice)  # Salida: 5

# Buscar la subcadena a partir de un índice específico
indice_desde = texto.find("mundo", 10)
print(indice_desde)  # Salida: 26

# Buscar la subcadena dentro de un rango específico
indice_rango = texto.find("Python", 15, 50)
print(indice_rango)  # Salida: 35

# Buscar una subcadena que no existe
indice_no_existe = texto.find("Java")
print(indice_no_existe)  # Salida: -1



#JOIN-------------------------------------------------------------------------------------------------------------
#Devuelve una cadena resultante de concatenar las cadenas de la secuencia se
#que separadas por la cadena sobre la que se llama el método.


# Lista de palabras
palabras = ['Hola', 'mundo', 'Python']

# Unir las palabras con un espacio como separador
frase = ' '.join(palabras)
print(frase)  # Salida: "Hola mundo Python"

# Unir con un separador de coma
frase_comas = ', '.join(palabras)
print(frase_comas)  # Salida: "Hola, mundo, Python"



#PARTITION-------------------------------------------------------------------------------------------------------------
#Busca el separador sep en la cadena y devuelve una tupla con la subcadena
#hasta dicho separador, el separador en si, y la subcadena del separador hasta
#el final de la cadena. Si no se encuentra el separador, la tupla contendrá la
#cadena en si y dos cadenas vacías.


texto = "nombre:usuario"

# Usar partition para dividir la cadena en el primer ':'
partes = texto.partition(':')
print(partes)  # Salida: ('nombre', ':', 'usuario')


texto = "nombreusuario"

# Intentar dividir la cadena donde no hay ':'
partes = texto.partition(':')
print(partes)  # Salida: ('nombreusuario', '', '')



#REPLACE-------------------------------------------------------------------------------------------------------------
#Devuelve una cadena en la que se han reemplazado todas las ocurrencias de la
#cadena old por la cadena new. Si se especifica el parámetro count, este indica
#el número máximo de ocurrencias a reemplazar.


texto = "Hola mundo, mundo"
nuevo_texto = texto.replace("mundo", "universo")
print(nuevo_texto)  # Salida: "Hola universo, universo"

#Reemplazo con Límite de Conteo
#Si solo deseas reemplazar un número limitado de ocurrencias, puedes usar el argumento count:
texto = "Hola mundo, mundo"
nuevo_texto = texto.replace("mundo", "universo", 1)
print(nuevo_texto)  # Salida: "Hola universo, mundo"


#Eliminación de Caracteres
#Puedes usar .replace() para eliminar caracteres o 
# subcadenas simplemente reemplazándolos por una cadena vacía:
texto = "Hola mundo"
texto_sin_o = texto.replace("o", "")
print(texto_sin_o)  # Salida: "Hla mund"



#SPLIT-----------------------------------------------------------------------------------------------------------------------------------------
#Devuelve una lista conteniendo las subcadenas en las que se divide nuestra
#cadena al dividirlas por el delimitador sep. En el caso de que no se especifique
#sep, se usan espacios. Si se especifica maxsplit, este indica el número máximo
#de particiones a realizar.




texto = "Hola mundo, bienvenidos a Python"
# División por espacios en blanco
partes = texto.split()
print(partes)  # Salida: ['Hola', 'mundo,', 'bienvenidos', 'a', 'Python']


texto = "uno,dos,tres,cuatro"
# División usando coma como separador
partes = texto.split(',')
print(partes)  # Salida: ['uno', 'dos', 'tres', 'cuatro']

texto = "uno dos tres cuatro"
# División con un máximo de 2 divisiones
partes = texto.split(' ', maxsplit=2)
print(partes)  # Salida: ['uno', 'dos', 'tres cuatro']





