#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------

class automovil:
    llantas=4
    def __init__(self, marca,vel):
        self.marca=marca
        self.velMax=vel

    def avanzar(self):
        print(f"el automovil '{self.marca}' avanzo con una velocidad inicial de: {self.velMax/12} km/hr")

carro1=automovil("audi",300)

carro1.avanzar()





