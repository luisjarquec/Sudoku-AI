tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def es_valido(tablero, fila, columna, num):
    if num in tablero[fila]: 
        return False

    if num in [tablero[i][columna] for i in range (9)]:
        return False
    
    fila_inicio, columna_inicio = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(fila_inicio, fila_inicio+3):
        for x in range(columna_inicio, columna_inicio+3):
            if tablero[i][x] == num: return False

    return True

def resolver_sudoku(tablero):
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                for numero in range (1,10):
                    if es_valido(tablero, fila, columna, numero):
                        tablero[fila][columna] = numero
                        if resolver_sudoku(tablero):
                            return True
                    tablero[fila][columna] = 0
                return False
    return True

if __name__ == '__main__':
    if resolver_sudoku(tablero):
        for fila in tablero:
            print(fila)
    else:
        print("No hay solución para este sudoku")


