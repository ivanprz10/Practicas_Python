#crea un programa en python que reciba 2 enteros introducidos por teclado y maneje la excepcion
try:
    var = 10/0
    print(var)
except ZeroDivisionError:
    print("error")

    
    class Mi_excepcion(BaseException):
        def _init_(self, *args: object) -> None:
            super()._init_(*args)
    
def division(num):
    if num==0:
        raise Mi_excepcion("excepcion personalizada")
    else:
        print(" bien")


division(0)



