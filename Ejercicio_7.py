"""Dada una matriz de MxN elementos, calcular el promedio de cada fila y de cada columna. Mostrar en pantalla la matriz cargada y los promedios correspondientes"""

import numpy as np

def calcular_promedio_filas(matriz):
    promedio_f = np.mean(matriz, axis=1)
    return promedio_f

def calcular_promedio_columnas(matriz):
    promedio_c = np.mean(matriz, axis=0)
    return promedio_c

n_filas = int(input("Ingresa número de filas: "))
n_columnas = int(input("Ingresa número de columnas: "))

matriz = np.zeros((n_filas, n_columnas))

for fila in range(n_filas):
    for columna in range(n_columnas):
        matriz[fila, columna] = int(input(f"Ingrese valor ({fila+1}, {columna+1}): "))

print(matriz)

promedio_filas = calcular_promedio_filas(matriz)
promedio_columnas = calcular_promedio_columnas(matriz)

for i in range(n_filas):
    print(f"Promedio fila {i+1}: {promedio_filas[i]}")

for j in range(n_columnas):
    print(f"Promedio columna {j+1}: {promedio_columnas[j]}")
