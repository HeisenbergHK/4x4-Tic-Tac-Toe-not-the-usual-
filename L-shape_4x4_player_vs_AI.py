import math

dimension = 4

board = [[' ' for j in range(dimension)] for i in range(dimension)]


def show_board(board):
    for row in board:
        print(row)


def is_win(board, mark):
    return check_l_shape_win(board, mark)


def check_l_shape_win(board, mark):
    dimension = 4
    # Define the 2D list to hold the coordinates of the L shapes in each state
    # Using the format (row, col) for coordinates, assuming (1,1) is top-left

    l_shapes = [
        # 1
        [(1, 1), (1, 2), (1, 3), (2, 1)],
        [(1, 2), (1, 3), (1, 4), (2, 2)],
        [(1, 1), (1, 2), (1, 3), (2, 3)],
        [(1, 2), (1, 3), (1, 4), (2, 4)],

        # 2
        [(2, 1), (2, 2), (2, 3), (3, 1)],
        [(2, 2), (2, 3), (2, 4), (3, 2)],
        [(2, 1), (2, 2), (2, 3), (3, 3)],
        [(2, 2), (2, 3), (2, 4), (3, 4)],

        # 3
        [(3, 1), (3, 2), (3, 3), (4, 1)],
        [(3, 2), (3, 3), (3, 4), (4, 2)],
        [(3, 1), (3, 2), (3, 3), (4, 3)],
        [(3, 2), (3, 3), (3, 4), (4, 4)],

        # 4
        [(2, 1), (2, 2), (2, 3), (1, 1)],
        [(2, 2), (2, 3), (2, 4), (1, 2)],
        [(2, 1), (2, 2), (2, 3), (1, 3)],
        [(2, 2), (2, 3), (2, 4), (1, 4)],

        # 5
        [(3, 1), (3, 2), (3, 3), (2, 1)],
        [(3, 2), (3, 3), (3, 4), (2, 2)],
        [(3, 1), (3, 2), (3, 3), (2, 3)],
        [(3, 2), (3, 3), (3, 4), (2, 4)],

        # 6
        [(4, 1), (4, 2), (4, 3), (3, 1)],
        [(4, 2), (4, 3), (4, 4), (3, 2)],
        [(4, 1), (4, 2), (4, 3), (3, 3)],
        [(4, 2), (4, 3), (4, 4), (3, 4)],

        # 1
        [(1, 1), (2, 1), (3, 1), (1, 2)],
        [(1, 2), (2, 2), (3, 2), (1, 3)],
        [(1, 3), (2, 3), (3, 3), (1, 4)],
        [(1, 2), (2, 2), (3, 2), (1, 1)],
        [(1, 3), (2, 3), (3, 4), (1, 2)],
        [(1, 4), (2, 4), (3, 4), (1, 3)],

        # 2
        [(2, 1), (3, 1), (4, 1), (2, 2)],
        [(2, 2), (3, 2), (4, 2), (2, 3)],
        [(2, 3), (3, 3), (4, 3), (2, 4)],
        [(2, 2), (3, 2), (4, 2), (2, 1)],
        [(2, 3), (3, 3), (4, 4), (2, 2)],
        [(2, 4), (3, 4), (4, 4), (2, 3)],

        # 3
        [(1, 1), (2, 1), (3, 1), (3, 2)],
        [(1, 2), (2, 2), (3, 2), (3, 3)],
        [(1, 3), (2, 3), (3, 3), (3, 4)],
        [(1, 2), (2, 2), (3, 2), (3, 1)],
        [(1, 3), (2, 3), (3, 3), (3, 2)],
        [(1, 4), (2, 4), (3, 4), (3, 3)],

        # 4
        [(2, 1), (3, 1), (4, 1), (4, 2)],
        [(2, 2), (3, 2), (4, 2), (4, 3)],
        [(2, 3), (3, 3), (4, 3), (4, 4)],
        [(2, 2), (3, 2), (4, 2), (4, 1)],
        [(2, 3), (3, 3), (4, 3), (4, 2)],
        [(2, 4), (3, 4), (4, 4), (4, 3)],
    ]

    for shape in l_shapes:
        if all(1 <= row <= dimension and 1 <= col <= dimension and board[row-1][col-1] == mark for row, col in shape):
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


def miniMax(board, player, depth, max_depth, alpha, beta):
    if is_win(board, 'X'):
        return 100 - depth
    elif is_win(board, 'O'):
        return -100 + depth
    elif not get_empty_cells(board):
        return 0
    elif depth == max_depth:
        return 0

    if player == 'X':
        best_score = -math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1, max_depth, alpha, beta)
            board[i][j] = ' '
            best_score = max(score, best_score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1, max_depth, alpha, beta)
            board[i][j] = ' '
            best_score = min(score, best_score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score


def find_best_move(board, player, max_depth):
    best_move = None
    best_score = -math.inf if player == 'X' else math.inf
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = player
        score = miniMax(board, change_player(player), 0, max_depth, -math.inf, math.inf)
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

    if current_player == 'X':
        try:
            i = int(input(f'Enter row (1-{dimension}): ')) - 1
            j = int(input(f'Enter col (1-{dimension}): ')) - 1
        except ValueError:
            print('---')
            print('Enter a number!')
            print('---')
            continue
    else:
        i, j = find_best_move(board, current_player, max_depth=7)

    if 0 <= i < dimension and 0 <= j < dimension:
        if is_empty(board, i, j):
            board[i][j] = current_player

            if is_win(board, current_player):
                print('---------------')
                show_board(board)
                print(f'{current_player} won!')
                break
            elif not get_empty_cells(board):
                print('---------------')
                show_board(board)
                print('Draw!')
                break

            current_player = change_player(current_player)
        else:
            print()
            print('The cell is already occupied!')
            print()
    else:
        print('---')
        print('Not in the range!')
        print('---')
