sudoku = [
[2,9,0,5,0,0,4,0,0],
[0,8,0,3,7,0,5,9,0],
[4,0,0,2,9,0,0,3,6],
[0,0,0,0,5,0,0,0,7],
[0,7,0,8,0,0,3,4,9],
[0,3,4,0,6,0,0,0,8],
[3,0,8,0,0,0,7,0,5],
[0,6,0,0,0,0,1,8,0],
[7,0,5,0,0,0,9,2,4]]


def print_sudoku(sudoku):
    for p in sudoku:
        print(p)
    return

def encontrar_coordenada_cuadro3x3(val): #horizontal pos. square
	if val <= 2:
		return 0
	elif val <= 5:
		return 1
	else:
		return 2

def obtener_cuadro_para_celda(x, y, sudoku):
    poscuadro_columna = encontrar_coordenada_cuadro3x3(x)
    poscuadro_fila = encontrar_coordenada_cuadro3x3(y)
    cuadro = []
    for fila in sudoku[poscuadro_fila *3: poscuadro_fila *3 + 3]:
        for columna in fila[poscuadro_columna *3: poscuadro_columna *3 + 3]:
            cuadro.append(columna)
            return cuadro

def se_ejecuta(x, y, v, sudoku):
	# Revisar la fila (horizontal)
	if v in sudoku[y]:
		return False
	# revisar la columna (vertical)
	columna = [fila[x] for fila in sudoku]
	if v in columna:
		return False
	# Revisar subcuadro 3x3
	cuadro3x3 = obtener_cuadro_para_celda(x, y, sudoku)
	if v in cuadro3x3:
		return False
	return True
def imprimir_sudoku(sudoku, val):
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for valor in range(1,10):
                    if se_ejecuta(x, y, valor, sudoku):
                        sudoku[y][x] = valor
                        imprimir_sudoku(sudoku, True)
                        sudoku[y][x] = 0
                return#-> imprimir_sudoku(sudoku, 1) ->sudoku[y][x] = 0
    # return "NOPE"
    print_sudoku(sudoku)
    print("----------------------------")

imprimir_sudoku(sudoku, False)
