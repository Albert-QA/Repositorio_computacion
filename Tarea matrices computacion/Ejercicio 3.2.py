import numpy as np

# Creamos una matriz aleatoria de 7 filas y 7 columnas con valores entre 0 y 100
matriz_aleatoria = np.random.randint(0, 101, size=(7, 7))

# Normalizamos la matriz entre 0 y 1
matriz_normalizada = (matriz_aleatoria - matriz_aleatoria.min()) / (matriz_aleatoria.max() - matriz_aleatoria.min())

# Imprimimos la matriz normalizada
print(matriz_normalizada)
