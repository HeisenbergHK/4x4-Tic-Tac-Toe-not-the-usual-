import math

dimension = 5

board = [[' ' for j in range(dimension)] for i in range(dimension)]


def show_board(board):
    for row in board:
        print(row)


def is_win(board, mark):
    return check_row_win(board, mark) or check_col_win(board, mark) or check_diagonal_win(board, mark)


def check_row_win(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    return False


def check_col_win(board, mark):
    for col in range(dimension):
        if all(board[row][col] == mark for row in range(dimension)):
            return True
    return False


def check_diagonal_win(board, mark):
    if all(board[i][i] == mark for i in range(dimension)):
        return True
    if all(board[i][dimension - 1 - i] == mark for i in range(dimension)):
        return True
    return False


def change_player(player):
    return 'O' if player == 'X' else 'X'


def is_empty(board, i, j):
    return board[i][j] == ' '


def get_empty_cells(board):
    empty_cells = []
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells


def miniMax(board, player, depth, max_depth):
    if is_win(board, 'X'):
        return 100 - depth
    elif is_win(board, 'O'):
        return -100 + depth
    elif not get_empty_cells(board):
        return 0
    elif depth == max_depth:
        return depth

    if player == 'X':
        best_score = -math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1, max_depth)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1, max_depth)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score


def find_best_move(board, player, max_depth):
    best_move = None
    best_score = -math.inf if player == 'X' else math.inf
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = player
        score = miniMax(board, change_player(player), 0, max_depth)
        board[i][j] = ' '
        if player == 'X':
            if score > best_score:
                best_score = score
                best_move = cell
        else:
            if score < best_score:
                best_score = score
                best_move = cell
    return best_move


current_player = 'X'

while True:
    print(f"{current_player}'s turn.")
    show_board(board)

    i, j = find_best_move(board, current_player, max_depth=3)

    if 0 <= i < dimension and 0 <= j < dimension:
        if is_empty(board, i, j):
            board[i][j] = current_player

            if is_win(board, current_player):
                print(f'{current_player} won!')
                show_board(board)
                break
            elif not get_empty_cells(board):
                print('Draw!')
                show_board(board)
                break

            current_player = change_player(current_player)
        else:
            print()
            print('The house is full!!!')
            print()
    else:
        print('---')
        print('Not in the range!')
        print('---')
