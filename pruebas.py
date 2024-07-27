#USO SOLO PARA PRUEBAS DE CODIGO EN PYTHON
#---------------------------------------------------------------------------------------------------------------

tam=int(input("¿de que tamaño sera su lista?"))
lista=[]
for i in range(tam):
    valor = int(input(f"ingrese el valor ({i+1}): "))
    lista.append(valor)

print(f"la lista orignal es {lista}")


lista.sort()
print(f"la lista ordenada es {lista}")

lista.reverse()
print(f"la lista en orden inverso es {lista}")

















