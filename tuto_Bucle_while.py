#Tutorial de como funciona el bucle While en Python------------
#mientras que una condicion se cumpla sea verdadera (True)
#esta seccion de codigo se ejecutara un numero de n veces hasta que se deje de cumplir
#o en otros casos sera infinito

edad = 0 #inicializamos una variable en este caso "edad" igual a cero

while edad < 18: #mientras que edad sea menor que 18 se cumplira la condicion es decir (True)
    print("eres menor de edad, tienes: ", edad) #se ejecuta el comando y se imprime la edad
    edad = edad + 1                             #aqui la edad cada vez que se repite el bucle se suma uno mas
                                                #es decir si la edad vale 2 se suma uno y se repite el bucle
print("Felicidades, eres mayor de edad", edad)  #aqui, al dejar de cumplirse la condicion se ejecuta lo que esta fuera
                                                #de mi bucle While