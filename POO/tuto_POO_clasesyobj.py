#TUTORIAL SENCILLO DE COMO CREAR UN PROGRAMA EN PYTHON ENFOCADO A POO
#CREACION DE CLASES Y OBJETOS
class automovil:
    llantas=4
    def __init__(self, marca,vel):
        self.marca=marca
        self.velMax=vel

    

carro1=automovil("audi",300)
print(carro1.llantas, carro1.marca, carro1.velMax)


#------------------------------------------------------------------------------------------------------------------------
#METODOS
class automovil:
    llantas=4
    def __init__(self, marca,vel):
        self.marca=marca
        self.velMax=vel

    def avanzar(self):
        print(f"el automovil '{self.marca}' avanzo con una velocidad inicial de: {self.velMax/12} km/hr")

carro1=automovil("audi",300)

carro1.avanzar()

#--------------------------------------------------------------------------------------------------------------------------------------
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
    super(vehiculos)


carro=vehiculos()

carro.arrancar()
