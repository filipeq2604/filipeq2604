"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None

    contarx = 0
    contaro = 0

    for line in board:
        for element in line:
            if element == X:
                contarx += 1
            elif element == O:
                contaro += 1

    if contarx <= contaro:
        print("É a vez do jogador X")
        return X
    else:
        print("É a vez do jogador O")
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    I'll implement to return a set of coordinates(x,y) of available moves
    """
    coordinates = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                coordinates.append((i, j))

    return coordinates


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print("Funcao RESULT")
    print(board)
    i = action[0]
    j = action[1]
    new_board = []
    for line in board:
        new_board.append(line[:])

    new_board[i][j] = player(board)
    print("DEPOIS")
    print(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    vencedor = utility(board)
    if vencedor == 1:
        print("O vencedor é o " + X)
        return X

    if vencedor == -1:
        print("O vencedor é o " + O)
        return O

    print("Deu empate")
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if utility(board) != 0:
        return True

    for line in board:
        for element in line:
            if element == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    '''Verificar na diagonal'''
    if (board[0][0] == board[1][1] == board[2][2] == X):
        return 1;

    if (board[0][0] == board[1][1] == board[2][2] == O):
        return -1;

    if (board[0][2] == board[1][1] == board[2][0] == X):
        return 1;

    if (board[0][2] == board[1][1] == board[2][0] == O):
        return -1;

    '''Verificar nas linhas e colunas'''
    for i in range(3):
        '''Verificando o jogo acabou nas linhas'''
        if (board[i][0] == board[i][1] == board[i][2] == X):
            return 1;

        if (board[i][0] == board[i][1] == board[i][2] == O):
            return -1;

        '''Verificando o jogo acabou nas colunas'''
        if (board[0][i] == board[1][i] == board[2][i] == X):
            return 1;

        if (board[0][i] == board[1][i] == board[2][i] == O):
            return -1;

    '''Caso nao tenha encontrado um vencedor vamos retorna 0'''
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print("Funcao MINIMAX")
    print(board)
    if terminal(board):
        return None

    acoes = actions(board)
    melhor_acao = acoes[0]

    if player(board) == X:
        melhor = -9999999999999999
        for acao in acoes:
            m = maxvalue(result(board, acao))
            if m > melhor:
                melhor = m
                melhor_acao = acao

    else:
        melhor = 9999999999999999
        for acao in acoes:
            movimento = result(board, acao)
            m = maxvalue(movimento)
            if m < melhor:
                melhor = m
                melhor_acao = acao

    return melhor_acao


def minvalue(board):
    print("minvalue")
    if terminal(board):
        return utility(board)

    v = 99999999999999999

    for acao in actions(board):
        v = min(v, maxvalue(result(board, acao)))

    return v


def maxvalue(board):
    print("maxvalue")
    if terminal(board):
        return utility(board)

    v = -99999999999999999

    for acao in actions(board):
        v = max(v, minvalue(result(board, acao)))

    return v
