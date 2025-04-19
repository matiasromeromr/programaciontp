"""Dada una matriz NxM, determinar si es una matriz simétrica."""

def es_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    if filas != columnas:
        return False

    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] != matriz[columna][fila]:
                return False
    return True

fila_matriz = int(input("Ingrese cantidad de filas: "))

columna_matriz = int(input("Ingrese cantidad de columnas: "))

if fila_matriz == columna_matriz:
    matriz_generada = []
    for i in range(fila_matriz):
        matriz_generada.append([0] * columna_matriz)

    for fila in range(fila_matriz):
        for columna in range(columna_matriz):
            matriz_generada[fila][columna] = float(input(f"Ingrese número {fila}, {columna}: "))

    if es_simetrica(matriz_generada):
        print("La matriz es simétrica")
    
    else:
        print("La matriz no es simétrica")

else:
    print("La matriz no es simétrica")