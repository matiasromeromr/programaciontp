"""Dada una lista N de números enteros y un número entero K, insertar K a la derecha de cada múltiplo de K"""

def cantidad_numeros():
    cantidad = int(input("Ingrese cantidad de valores que desea agregar a la lista: "))
    return cantidad

def pedir_numerok():
    numerok = int(input("Ingrese un número entero K: "))
    return numerok

def agregar_a_lista(cantidad):
    lista = []
    for i in range(cantidad):
        numero_ingresado = int(input("Ingrese un número: "))
        lista.append(numero_ingresado)
    return lista

cantidad = cantidad_numeros()

lista_ingresos = agregar_a_lista(cantidad)

numero_k = pedir_numerok()

nueva_lista = []
for numero in lista_ingresos:
    nueva_lista.append(numero)
    if numero % numero_k == 0:
        nueva_lista.append(numero_k)

print("Lista original",lista_ingresos)

print("Lista nueva:", nueva_lista)