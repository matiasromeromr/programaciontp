"""Dado un vector con N dígitos, invertir sus elementos considerando lo siguiente:
b) Sin usar un vector auxiliar"""

def cantidad_numeros():
    cantidad = int(input("¿Cuántos números desea agregar a la lista?: "))
    return cantidad

def ingresar_numero():
    lista_numeros = []
    cantidad = cantidad_numeros()
    for i in range(cantidad):
        numero_ingresado = int(input("Ingrese número: "))
        lista_numeros.append(numero_ingresado)
    return lista_numeros

def invertir_lista(lista_numeros):
    lista_numeros.reverse()
    return lista_numeros 

lista_numeros = ingresar_numero() 
print("Lista inicial:", lista_numeros)

nueva_lista = invertir_lista(lista_numeros)
print("Lista invertida:", nueva_lista)