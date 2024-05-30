import numpy as np

# Creamos un array de 7 filas y 8 columnas lleno de ceros de tipo entero
array_ceros = np.zeros((7, 8), dtype=int)

# Creamos un array de 1 fila y 8 columnas lleno de unos de tipo entero
array_unos = np.ones((1, 8), dtype=int)

# Insertamos el array de unos en la primera fila del array de ceros
array_ceros[0, :] = array_unos

# Imprimimos el array
print(array_ceros)
