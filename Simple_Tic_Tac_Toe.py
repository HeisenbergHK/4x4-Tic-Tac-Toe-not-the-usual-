"""
/******************************************************************************
 *  File:           Tic Tac Toe
 *  Author:         Hassan Kalantari
 *  Email:          hasan.kalantari29@gmail.com
 *  GitHub:         HeisenbergHK
 *  Description:    This is the old fashion Tic Tac Toe game but in a 4x4 board
                    and the winning condition is not having all the X's or O's in
                    a row, but creating an L shape using 4 marks
 *  Last Modified: (May 14, 2024)
 *****************************************************************************/
"""
import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH = 500
HEIGHT = 500
LINE_WIDTH = 15
BOARD_ROWS = 4
BOARD_COLS = 4
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (0, 0, 0)
MESSAGE_BOX_COLOR = (200, 200, 200)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


# Draw the grid
def draw_grid():
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (3 * SQUARE_SIZE, 0), (3 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (4 * SQUARE_SIZE, 0), (4 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 3 * SQUARE_SIZE), (WIDTH, 3 * SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 4 * SQUARE_SIZE), (WIDTH, 4 * SQUARE_SIZE), LINE_WIDTH)


# Draw the Xs and Os
def draw_board(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE + 20, row * SQUARE_SIZE + 20),
                                 ((col + 1) * SQUARE_SIZE - 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, ((col + 1) * SQUARE_SIZE - 20, row * SQUARE_SIZE + 20),
                                 (col * SQUARE_SIZE + 20, (row + 1) * SQUARE_SIZE - 20), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (int(col * SQUARE_SIZE + SQUARE_SIZE / 2),
                                                   int(row * SQUARE_SIZE + SQUARE_SIZE / 2)), 45, int(LINE_WIDTH / 1.5))


# Check if player is won?
def is_win(size, player, board):
    for i in range(size):
        for j in range(size):
            if board[i][j] == player:
                # This will check for all horizontal L's
                if j + 2 < size:
                    if 0 < i < size - 1:
                        if board[i][j + 1] == player and board[i][j + 2] == player:
                            if board[i + 1][j + 2] == player or board[i - 1][j + 2] == player or board[i - 1][j] == player or board[i + 1][
                                j] == player:
                                return True
                            else:
                                return False
                    elif i == 0:
                        if board[i][j + 1] == player and board[i][j + 2] == player:
                            if board[i + 1][j + 2] == player or board[i + 1][j] == player:
                                return True
                            else:
                                return False
                    elif i == size - 1:
                        if board[i][j + 1] == player and board[i][j + 2] == player:
                            if board[i - 1][j + 2] == player or board[i - 1][j] == player:
                                return True
                            else:
                                return False
                # This will check for all vertical L's
                if i + 2 < size:
                    if 0 < j < size - 1:
                        if board[i + 1][j] == player and board[i + 2][j] == player:
                            if board[i + 2][j + 1] == player or board[i + 2][j - 1] == player or board[i][j + 1] == player or board[i][
                                j - 1] == player:
                                return True
                            else:
                                return False
                    elif j == 0:
                        if board[i + 1][j] == player and board[i + 2][j] == player:
                            if board[i + 2][j + 1] == player or board[i][j + 1] == player:
                                return True
                            else:
                                return False
                    elif size - 1:
                        if board[i + 1][j] == player and board[i + 2][j] == player:
                            if board[i + 2][j - 1] == player or board[i][j - 1] == player:
                                return True
                            else:
                                return False


# H
def is_board_full(board):
    for row in board:
        for i in row:
            if i == '':
                return False
    return True


# Display winning message
def display_winner(winner):
    font = pygame.font.Font(None, 36)
    if winner == 'X' or winner == 'O':
        text = font.render(f"{winner} wins!", True, BLACK)
    else:
        text = font.render(f"{winner}", True, BLACK)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    pygame.draw.rect(screen, MESSAGE_BOX_COLOR, (WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)


# Main game loop
board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 'X'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0] // SQUARE_SIZE
            mouseY = event.pos[1] // SQUARE_SIZE

            if board[mouseY][mouseX] == '':
                board[mouseY][mouseX] = player
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'

            print(board)

    screen.fill(WHITE)
    draw_grid()
    draw_board(board)
    if is_board_full(board):
        display_winner("It's a draw!")
    elif is_win(BOARD_COLS, 'X', board):
        display_winner('X')
    elif is_win(BOARD_COLS, 'O', board):
        display_winner('O')

    pygame.display.update()
    if is_board_full(board) or is_win(BOARD_COLS, 'X', board) or is_win(BOARD_COLS, 'O', board):
        pygame.time.delay(2000)  # Delay for 2 seconds
        break
