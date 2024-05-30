tablero = [[1 if (row + col) % 2 != 0 else 0 for col in range(8)] for row in range(8)]
print("Tablero de ajedrez:")
for row in tablero:
    print(row)
    