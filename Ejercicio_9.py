"""Para una matriz A de MxN, y dos valores k y h, indicar si el elemento A[k, h] es un punto silla."""

def generar_matriz(tamaño):
    matriz = []

    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            valor = int(input(f"Ingrese el valor de la posición ({i+1}, {j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    return matriz

def punto_silla(matriz, indice_fila, indice_columna):
    
    fila_minima = min(matriz[indice_fila])

    columna_maxima = max(matriz[i][indice_columna] for i in range(len(matriz)))

    if matriz[indice_fila][indice_columna] == fila_minima and matriz[indice_fila][indice_columna] == columna_maxima:
        return True
    
    else:
        return False

tamaño = int(input("Ingrese el tamaño de la matriz: "))

matriz = generar_matriz(tamaño)

indice_fila = int(input("Ingrese el índice de la fila: ")) - 1

indice_columna = int(input("Ingrese el índice de la columna: ")) - 1

if punto_silla(matriz, indice_fila, indice_columna):
    print(f"El elemento en la posición ({indice_fila+1}, {indice_columna+1}) es un punto silla.")

else:
    print(f"El elemento en la posición ({indice_fila+1}, {indice_columna+1}) no es un punto silla.")