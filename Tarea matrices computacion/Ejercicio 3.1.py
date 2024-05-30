import numpy as np

# Creamos una matriz aleatoria de 7 filas y 7 columnas con valores entre 0 y 100
matriz_aleatoria = np.random.randint(0, 101, size=(7, 7))

# Imprimimos la matriz aleatoria
print(matriz_aleatoria)

# Calculamos el valor mínimo de la matriz
valor_minimo = matriz_aleatoria.min()

# Imprimimos el valor mínimo
print(f"Valor mínimo: {valor_minimo}")

# Calculamos el valor máximo de la matriz
valor_maximo = matriz_aleatoria.max()

# Imprimimos el valor máximo
print(f"Valor máximo: {valor_maximo}")
