#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------
class automovil:
    numLlantas=4
    espejos =2
    def __init__(self, marca, vel):
        
        self.marca=marca
        self.velMax=vel
    def avanzar(self):
        print(f"el carro {self.marca}, inicio con una velocidad de {self.velMax/10}km/hr")



carro = automovil("audi", 280)
carro2 = automovil("BMW",200)

print(f"el automovil {carro.marca} tiene {carro.numLlantas} llantas y tiene una velocidad maxima de {carro.velMax} km/hr")
carro.avanzar()
print(f"el automovil {carro2.marca} tiene {carro2.numLlantas} llantas y tiene una velocidad maxima de {carro2.velMax} km/hr")


