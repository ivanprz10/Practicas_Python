#La encapsulación se refiere a impedir el acceso a determinados métodos y
#atributos de los objetos estableciendo así qué puede utilizarse desde fuera de la clase.

class vehiculos:
    def __init__(self,mar,velocidadMax,modelo):#todos los atributos de la clase quedaron privados
        self.__marca=mar
        self.__velMax=velocidadMax
        self.__modelo=modelo

    def atributos(self):
        print(f"el automovi marca:  {self.__marca}")
        print(f"tiene una velocidad maxima de: {self.__velMax}km/hr")
        print(f"es el modelo: {self.__modelo}")
        carro.__arrancar()
        

    def __arrancar(self):#metodo privado solo se puede acceder a el desde la misma clase
        arrancar = int(self.__velMax/12)
        print(f"el automovil {self.__marca} inicia con una velocidad de: {arrancar}km/hr")
        

carro=vehiculos("audi",200,"A8")

carro.atributos()


#------------------------------------------------------------------------------------------------------------------------
#GETTER Y SETTER
#GET=OBTENER
#SET = ASIGNAR
class persona():
    def __init__(self, nom, apep,apem):
        self.__nombre=nom
        self.__apellidop=apep
        self.__apellidom=apem
    
    def atributos(self):
        print(f"el nombre es: {self.__nombre}")
        print(f"el apellido paterno es {self.__apellidop}")
        print(f"el apellido materno es {self.__apellidom}")
    
    #getter
    def get_nombre(self):
        return self.__nombre
    def get_apellidop(self):
        return self.__apellidop
    def get_apellidom(self):
        return self.__apellidom

    #setter
    def set_nombre(self,nomb):
        self.__nombre=nomb
    def set_apellidop(self,app):
        self.__apellidop=app
    def set_apellidom(self,apm):
        self.__apellidom=apm

sujeto=persona("ivan","perez","cruz")

sujeto.set_nombre("juan")
print(sujeto.get_nombre())
