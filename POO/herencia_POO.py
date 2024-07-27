#TUTORIAL PARA ENTENDER LA HERENCIA, PILAR DE LA POO
#Cada que querramos crear una clase que este relacionada con otra clase 
#podemos crear una clase hija o subclase que herede atributos y metodos de la clase principal

class Vehiculos:#clase padre o super clase
    pass

class motocicletas(Vehiculos):#clase hija o subclase
    pass

class carro(Vehiculos):#clase hija o subclase
    pass


#----------------------------------------------------------------------------------------------------------------------
#ejemplo de herencia con una clase 

class vehiculos:#definimos una clase vehiculos 
    def __init__(self,marca,velocidadMax,modelo):#declaramos un constructor que inicialice atributos
        self.marca=marca
        self.velMax=velocidadMax
        self.modelo=modelo
        #atributos que pertenecen a toda clase de vehiculos

    def atributos(self):#definimos un metodo es decir una accion de los mismos  
        print(f"el automovi marca:  {self.marca}")
        print(f"tiene una velocidad maxima de: {self.velMax}km/hr")
        print(f"es el modelo: {self.modelo}")

    def arrancar(self):#definimos un metodo es decir una accion de los mismos
        arrancar = int(self.velMax/12)
        print(f"el automovil {self.marca} inicia con una velocidad de: {arrancar}km/hr")

class motocicleta(vehiculos):#definimos una clase motocicleta, si nos damos cuenta esta clase necesita heredar 
                             #atributos de la clase padre
    def __init__ (self,marca,velocidadMax,modelo,ruedas):#como esta clase tiene sus propios atributos
                                                         #declaramos un nuevo constructor para la misma

        super().__init__(marca,velocidadMax,modelo)#comando super() indicamos que de la superclase necesitaremos 
        self.ruedas=ruedas                         #elementos del constructor



moto=motocicleta("Vento",150,"Screamer",2)

moto.atributos()
print(moto.ruedas)

#---------------------------------------------------------------------------------------------------------------------------
#sobrescribir metodos

class vehiculos:
    def __init__(self,marca,velocidadMax,modelo):
        self.marca=marca
        self.velMax=velocidadMax
        self.modelo=modelo

    def atributos(self):
        print(f"el automovi marca:  {self.marca}")
        print(f"tiene una velocidad maxima de: {self.velMax}km/hr")
        print(f"es el modelo: {self.modelo}")

    def arrancar(self):
        arrancar = int(self.velMax/12)
        print(f"el automovil {self.marca} inicia con una velocidad de: {arrancar}km/hr")

class motocicleta(vehiculos):
    def __init__ (self,marca,velocidadMax,modelo,ruedas):
        super().__init__(marca,velocidadMax,modelo)
        self.ruedas=ruedas

    def arrancar(self):
        print(f"la moto {self.modelo} encendio, levanto la pata de seguridad y....")
        super().arrancar()



moto=motocicleta("Vento",150,"Screamer",2)

moto.arrancar()
