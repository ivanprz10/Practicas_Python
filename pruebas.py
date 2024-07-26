#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------
class personas:
    def __init__(self,nom,edad,sex):
        self.__nombre=nom
        self.__edad=edad
        self.__sexo=sex

    def mostrar (self):
        print(f"el nombre es: {self.__nombre}")
        print(f"la edad es: {self.__edad}")
        print(f"el sexo es: {self.__sexo}")


    #getter
    def get_nombre(self):
        return self.__nombre
    



    #setter
    def set_nombre(self,nuevo):
        self.__nombre=nuevo

obj1=personas("juanito",18,"masculino")
obj1.mostrar()
obj1.set_nombre(20)
obj1.mostrar()



