#Dados N números enteros cargados en un vector, todos distintos de cero, mostrar aquellos números que sean compuestos.

def verifica_compuesto(num):
    if num <= 1:
        compuesto = False
    else:
        cantidad_divisores = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cantidad_divisores += 1
        if cantidad_divisores > 2:
            compuesto = True
        else:
            compuesto = False
    return compuesto

def lista_compuestos(lista_numeros):
    numeros_compuestos = []
    for numero in lista_numeros:
        if verifica_compuesto(numero):
            numeros_compuestos.append(numero)
    return numeros_compuestos

cantidad_numeros = int(input("¿Cuántos números quiere agregar a la lista?: "))
numeros_ingresados = []

for i in range(cantidad_numeros):
    numero = int(input("Ingrese el número: "))
    numeros_ingresados.append(numero)

compuestos = lista_compuestos(numeros_ingresados)

print("Los números compuestos en su lista son:", compuestos)
