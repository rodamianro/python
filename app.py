from random import randrange
# Creamos el board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def DisplayBoard(board):
    """Imprime el tablero de juego

    Parámetros:

        board -- Estado del tablero 

    Imprime en pantalla el tablero en el estado que ingresa como parametro

    """
    print("+-------"*len(board), "+", sep="")
    for i in range(len(board)):
        print("|       "*len(board), "|", sep="")
        print("|", end="")
        for j in range(len(board[i])):
            print("   ", board[i][j], "   |", sep="", end="")
        print("")
        print("|       "*len(board), "|", sep="")
        print("+-------"*len(board), "+", sep="")

# la función acepta el estado actual del board y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el board acorde a la decisión del usuario


def EnterMove(board):
    """Pregunta al usuario el movimiento, lo verifica y actualiza el estado del tablero

    Parémtros:

        board -- Estado del tablero

    Retorna el nuevo estado del tablero
    """
    isNotOk = True
    while isNotOk:
        movimiento = int(input("Ingresa tu movimiento:"))
        if movimiento > 0 and movimiento < 10:

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == movimiento:
                        board[i][j] = 'X'
                        isNotOk = False

            if isNotOk:
                print("La posición ingresada no esta disponible")
        else:
            print("Opción invalida")

    return board

# la función examina el board y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna


def MakeListOfFreeFields(board):
    """Examina y construye una lista de los cuadros vacíos

    Parámetros:

        board -- Estado actual del tablero

    Examina el tablero y devuelve una lista con las posiciones vacias 
    """
    cuadrosVacios = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O' or board[i][j] == 'X':
                continue
            cuadrosVacios.append((i, j,))
    return cuadrosVacios

# la función analiza el estatus del board para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego


def VictoryFor(board, sign):
    """Verifica si el jugador a ganado

    Parámetros:

        boar -- Estado actual del tablero.
        sing -- Signo a comprobar ('O' o 'X')

    Retorna si el signo ingresado ha ganado (Boolean)
    """
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    if board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    if board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    if board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    if board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

# la función dibuja el movimiento de la maquina y actualiza el board


def DrawMove(board):
    """Dibuja el movimiento de la maquina

    Parámetros:

        board -- Estado actual del tablero

    Hace que la maquina seleccione una posición del tablero y la marca, retorna nuevo estado del tablero

    """
    isNotDone = True
    while isNotDone:
        posicion = randrange(1, 9)
        if len(MakeListOfFreeFields(board)) > 0:
            for i in range(len(board)):
                if posicion in board[i]:
                    for j in range(len(board)):
                        if board[i][j] == posicion:
                            board[i][j] = 'O'
                            isNotDone = False
                            break
                if not isNotDone:
                    break
        else:
            isNotDone = False
    return board


# Dibujamos el tablero inicial
DisplayBoard(board)
while True:
    # Ingresamos el movimiento del jugador
    board = EnterMove(board)
    # Dibujamos el tablero
    DisplayBoard(board)
    # Comprobamos si el jugador ya gano
    if VictoryFor(board, 'X'):
        print("Gano el jugador")
        break
    # Hacemos que la maquina marque una casilla
    board = DrawMove(board)
    # Dibujamos el tablero con el movimiento
    DisplayBoard(board)
    # Comprobamos si la maquina gano
    if VictoryFor(board, 'O'):
        print("Gano la maquina")
        break
    # Comprobamos si aún existen posibles movimientos
    if len(MakeListOfFreeFields(board)) == 0:
        break
