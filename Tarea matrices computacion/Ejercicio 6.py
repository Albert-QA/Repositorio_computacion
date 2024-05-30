import numpy as np

# Matriz original
original_matrix = np.array([
    [255, 34, 45, 16, 24, 99],
    [200, 50, 67, 15, 56, 88],
    [165, 67, 34, 26, 87, 70],
    [120, 100, 45, 45, 56, 67],
    [45, 225, 35, 67, 50, 44],
    [36, 255, 24, 78, 77, 23]
])

# Nueva submatriz
sub_matrix = np.array([
    [0, 0, 0],
    [0, 255, 0],
    [0, 0, 0]
])

# Función para reemplazar la submatriz en la matriz original
def replace_submatrix(matrix, sub_matrix, target_value):
    # Encontrar la posición del valor objetivo en la matriz original
    result = np.where(matrix == target_value)
    positions = list(zip(result[0], result[1]))
    
    for pos in positions:
        row, col = pos
        
        # Verificar si la submatriz cabe dentro de la matriz original
        if row + 1 < matrix.shape[0] and col + 1 < matrix.shape[1]:
            matrix[row-1:row+2, col-1:col+2] = sub_matrix
            
    return matrix

# Reemplazar la submatriz en la matriz original
new_matrix = replace_submatrix(original_matrix, sub_matrix, 50)

print(new_matrix)