import tkinter as tk
from tkinter import messagebox
import threading
import math

dimension = 4

# Initialize the board
board = [[' ' for _ in range(dimension)] for _ in range(dimension)]


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


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.current_player = 'X'
        self.buttons = [[None for _ in range(dimension)] for _ in range(dimension)]
        self.create_widgets()

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.root.quit()

    def create_widgets(self):
        for i in range(dimension):
            for j in range(dimension):
                button = tk.Button(self.root, text=' ', width=5, height=2, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def on_click(self, i, j):
        if board[i][j] == ' ' and self.current_player == 'X':
            board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if is_win(board, self.current_player):
                self.end_game(f'{self.current_player} won!')
            elif not get_empty_cells(board):
                self.end_game('Draw!')
            else:
                self.current_player = change_player(self.current_player)
                self.root.after(100, self.computer_move)

    def computer_move(self):
        thread = threading.Thread(target=self.calculate_best_move)
        thread.start()

    def calculate_best_move(self):
        move = find_best_move(board, 'O', max_depth=7)
        if move:
            i, j = move
            board[i][j] = 'O'
            self.root.after(100, lambda: self.buttons[i][j].config(text='O'))
            if is_win(board, 'O'):
                self.root.after(200, lambda: self.end_game('O won!'))
            elif not get_empty_cells(board):
                self.root.after(200, lambda: self.end_game('Draw!'))
            else:
                self.current_player = change_player(self.current_player)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    app = TicTacToeGUI(root)
    root.mainloop()
