# Programa 2: Ordenación de Arreglo Multidimensional

def ordenar_fila(matriz, fila):
    # Implementación de Bubble Sort para ordenar la fila especificada
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambio de elementos
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Matriz de ejemplo
matriz = [
    [9, 2, 7],
    [4, 5, 1],
    [6, 3, 8]
]

# Fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Llamamos a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz después de ordenar la fila:")
for fila in matriz:
    print(fila)