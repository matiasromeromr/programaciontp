"""Dada una lista A de N números reales, crear y mostrar una lista B con aquellos elementos de A que en su parte entera tenga: exactamente dos dígitos pares y al menos dos dígitos impares"""

def cantidad_numeros():
    cantidad = int(input("¿Cuántos números desea agregar a la lista?: "))
    return cantidad

def ingresar_numero():
    lista_numeros = []
    cantidad = cantidad_numeros()
    for i in range(cantidad):
        numero_ingresado = float(input("Ingrese un número real: "))
        lista_numeros.append(numero_ingresado)
    return lista_numeros

def obtener_parte_entera(numero):
    return abs(int(numero)) 

def cantidad_pares(parte_entera):
    pares = 0
    for i in str(parte_entera): 
        if int(i) % 2 == 0:
            pares += 1
    return pares

def cantidad_impares(parte_entera):
    impares = 0
    for i in str(parte_entera):
        if int(i) % 2 != 0:
            impares += 1
    return impares

def nueva_lista(lista_numeros):
    lista_reorganizada = []
    for numero in lista_numeros:
        parte_entera = obtener_parte_entera(numero)
        cant_pares = cantidad_pares(parte_entera)
        cant_impares = cantidad_impares(parte_entera)
        
        if cant_pares == 2 and cant_impares >= 2:
            lista_reorganizada.append(numero)
    
    return lista_reorganizada

lista_ingresados = ingresar_numero()
print("Su lista inicial es:", lista_ingresados)

lista_final = nueva_lista(lista_ingresados)
print("Los números que cumplen la condición son:", lista_final)
