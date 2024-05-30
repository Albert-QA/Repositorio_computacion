import numpy as np

# Creamos un array de 7 filas y 8 columnas
array = np.zeros((7, 8), dtype=int)

# Creamos un array con el rango entre 5 y 8
rango = np.arange(5, 9)

# Insertamos el rango en la última fila del array
array[-1, :] = rango

# Imprimimos el array
print(array)
