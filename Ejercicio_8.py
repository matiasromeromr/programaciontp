"""Dada una matriz cuadrada de MxM elementos enteros, realizar un programa que permita almacenar en un vector de K elementos, aquellos números de la matriz donde su factorial sea mayor o igual a la suma de la diagonal principal. Luego eliminar del vector resultante los elementos repetidos."""

import math

def generar_matriz(tamaño):
    matriz = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            valor = int(input(f"Ingrese el valor de la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def calcular_suma_diagonal(matriz):
    tamaño = len(matriz)
    suma_diagonal = sum(matriz[i][i] for i in range(tamaño))
    return suma_diagonal

tamaño_matriz = int(input("Ingrese cantidad de filas y columnas que tendrá la matriz: "))
matriz_generada = generar_matriz(tamaño_matriz)
suma_diagonal = calcular_suma_diagonal(matriz_generada)

nuevo_vector = []

for fila in matriz_generada:
    for numero in fila:
        if math.factorial(numero) >= suma_diagonal:
            nuevo_vector.append(numero)

vector_final = list(set(nuevo_vector))

print("El resultado de la suma de la diagonal principal es:", suma_diagonal)

print("El vector sin elementos repetidos es:", vector_final)