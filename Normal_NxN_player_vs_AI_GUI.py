import tkinter as tk
import math
import threading

dimension = 5
board = [[' ' for _ in range(dimension)] for _ in range(dimension)]

# Initialize the main window
root = tk.Tk()
root.title("L-Shape Tic-Tac-Toe")

current_player = 'X'
buttons = [[None for _ in range(dimension)] for _ in range(dimension)]


# Function to update the GUI board display
def update_buttons():
    for i in range(dimension):
        for j in range(dimension):
            buttons[i][j].config(text=board[i][j], state='normal' if board[i][j] == ' ' else 'disabled')


# Function to check if a player has won
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


# Function to check if a cell is empty
def is_empty(board, i, j):
    return board[i][j] == ' '


# Change the player after a move
def change_player(player):
    return 'O' if player == 'X' else 'X'


# MiniMax function (same as original, no change)
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


# Function to find the best move for AI
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


# Function to handle AI move in a separate thread
def ai_move():
    global current_player
    i, j = find_best_move(board, current_player, max_depth=3)
    board[i][j] = current_player
    update_buttons()
    check_game_status()


# Function for when a button is clicked
def button_click(i, j):
    global current_player
    if is_empty(board, i, j):
        board[i][j] = current_player
        update_buttons()

        if is_win(board, current_player):
            status_label.config(text=f"{current_player} wins!")
            disable_all_buttons()
        elif not get_empty_cells(board):
            status_label.config(text="Draw!")
            disable_all_buttons()
        else:
            current_player = change_player(current_player)
            status_label.config(text=f"{current_player}'s turn")
            if current_player == 'O':  # AI's turn
                lock_buttons()
                threading.Thread(target=ai_move).start()  # Run AI move in a separate thread


# Function to check the game status after each move
def check_game_status():
    global current_player
    if is_win(board, current_player):
        status_label.config(text=f"{current_player} wins!")
        disable_all_buttons()
    elif not get_empty_cells(board):
        status_label.config(text="Draw!")
        disable_all_buttons()
    else:
        current_player = change_player(current_player)
        status_label.config(text=f"{current_player}'s turn")
        if current_player == 'X':
            unlock_buttons()  # Human player's turn


# Disable all buttons after the game ends
def disable_all_buttons():
    for i in range(dimension):
        for j in range(dimension):
            buttons[i][j].config(state='disabled')


# Lock all buttons (used when AI is thinking)
def lock_buttons():
    for i in range(dimension):
        for j in range(dimension):
            buttons[i][j].config(state='disabled')


# Unlock all buttons (used when it's the human player's turn)
def unlock_buttons():
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == ' ':
                buttons[i][j].config(state='normal')


# Get empty cells for move calculations
def get_empty_cells(board):
    empty_cells = []
    for i in range(dimension):
        for j in range(dimension):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return empty_cells


# Create the game board buttons
for i in range(dimension):
    for j in range(dimension):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=5, command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Create a status label
status_label = tk.Label(root, text=f"{current_player}'s turn", font=('Helvetica', 16))
status_label.grid(row=dimension, column=0, columnspan=dimension)

# Start the GUI event loop
root.mainloop()