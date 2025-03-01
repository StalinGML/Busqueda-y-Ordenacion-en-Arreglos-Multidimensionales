# Programa 1: Búsqueda en Arreglo Multidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición (i, j) si se encuentra
    return None  # Si no se encuentra el valor

# Matriz bidimensional
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor a buscar
valor_buscado = 6

# Llamamos a la función
resultado = buscar_valor(matriz, valor_buscado)

# Mostramos el resultado
if resultado:
    print(f"El valor {valor_buscado} se encuentra en la posición {resultado}.")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")