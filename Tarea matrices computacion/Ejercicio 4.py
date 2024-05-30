import numpy as np

# Creamos la matriz
matriz = np.array([
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 9, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
])

# Creamos una máscara booleana para identificar los valores 9 y 1
mascara = np.where((matriz == 9) | (matriz == 1))

# Invertimos los valores 9 y 1 utilizando la función `where`
matriz[mascara] = np.where(mascara[0] == 1, 1, 9)

# Imprimimos la matriz
print(matriz)
