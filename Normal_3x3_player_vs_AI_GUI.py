import tkinter as tk
import math

dimension = 3
board = [[' ' for _ in range(dimension)] for _ in range(dimension)]


# Define game logic functions
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


def miniMax(board, player, depth):
    if is_win(board, 'X'):
        return 1
    elif is_win(board, 'O'):
        return -1
    elif not get_empty_cells(board):
        return 0

    if player == 'X':
        best_score = -math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for cell in get_empty_cells(board):
            i, j = cell
            board[i][j] = player
            score = miniMax(board, change_player(player), depth + 1)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score


def find_best_move(board, player):
    best_move = None
    best_score = -math.inf if player == 'X' else math.inf
    for cell in get_empty_cells(board):
        i, j = cell
        board[i][j] = player
        score = miniMax(board, change_player(player), 0)
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


# GUI setup
def on_button_click(i, j):
    global current_player
    if is_empty(board, i, j):
        board[i][j] = current_player
        buttons[i][j].config(text=current_player)

        if is_win(board, current_player):
            status_label.config(text=f"{current_player} won!")
            disable_buttons()
        elif not get_empty_cells(board):
            status_label.config(text="It's a draw!")
            disable_buttons()
        else:
            current_player = change_player(current_player)
            if current_player == 'O':  # Let the computer play
                i, j = find_best_move(board, current_player)
                on_button_click(i, j)


def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)


def reset_game():
    global board, current_player
    board = [[' ' for _ in range(dimension)] for _ in range(dimension)]
    current_player = 'X'
    for row in buttons:
        for button in row:
            button.config(text="", state=tk.NORMAL)
    status_label.config(text="Player X's turn.")


# Initialize tkinter
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize the game state
current_player = 'X'

# Create buttons for the Tic-Tac-Toe grid
buttons = [[None for _ in range(dimension)] for _ in range(dimension)]
for i in range(dimension):
    for j in range(dimension):
        buttons[i][j] = tk.Button(root, text="", width=10, height=3, font=('Arial', 24),
                                  command=lambda i=i, j=j: on_button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Add status label
status_label = tk.Label(root, text="Player X's turn", font=('Arial', 18))
status_label.grid(row=dimension, column=0, columnspan=dimension)

# Add reset button
reset_button = tk.Button(root, text="Reset", command=reset_game, font=('Arial', 14))
reset_button.grid(row=dimension + 1, column=0, columnspan=dimension)

# Start the tkinter main loop
root.mainloop()