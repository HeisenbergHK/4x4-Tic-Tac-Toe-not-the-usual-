# Tic-Tac-Toe Variations

This repository contains several variations of the Tic-Tac-Toe game, including traditional 3x3 boards, NxN customizable grids, and L-shaped boards. The games support both player-vs-player and player-vs-AI modes. Some versions also include a graphical user interface (GUI) built with tkinter.

## Notice
Please be aware that the performance of the AI algorithm may vary based on your computer’s processing power and the size of the board. For larger boards or less powerful machines, it may take some time for the algorithm to find the best move. We appreciate your patience while the AI computes its move.

## Files Overview
### Normal Tic-Tac-Toe
- **Normal_3x3_player_vs_AI.py**: A standard 3x3 Tic-Tac-Toe game where a human player competes against an AI using a minimax algorithm.
- **Normal_3x3_AI_vs_AI.py**: A standard 3x3 Tic-Tac-Toe game with AI playing against another AI using the minimax algorithm.
- **Normal_NxN_player_vs_AI.py**: An NxN version of Tic-Tac-Toe, where the board size is customizable, and a human player competes against an AI.
- **Normal_NxN_AI_vs_AI.py**: An NxN customizable grid with AI competing against another AI.
- **Normal_3x3_player_vs_AI_GUI.py**: A GUI version of the 3x3 player vs AI game.
- **Normal_NxN_player_vs_AI_GUI.py**: A GUI version of the NxN customizable player vs AI game.

### L-Shaped Tic-Tac-Toe

- **L-shape_4x4_player_vs_AI.py**: A 4x4 L-shaped board where a human player competes against an AI.
- **L-shape_4x4_player_vs_AI_GUI.py**: A GUI version of the 4x4 L-shaped player vs AI game.
- **L-shape_NxN_player_vs_AI_GUI.py**: A GUI version of the NxN customizable L-shaped player vs AI game (code example shown below).

### Simple Tic-Tac-Toe

- **Simple_Tic_Tac_Toe.py**: A minimal implementation of Tic-Tac-Toe for basic player-vs-player functionality.

### Features

- NxN board (customizable dimensions)
- Human vs AI gameplay
- AI moves calculated using the minimax algorithm
- GUI for ease of play
- Dynamic status updates (shows whose turn it is, who won, or if the game is a draw)

## Requirements

To run the games, install the necessary packages listed in `requirements.txt`.
You can install them by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

To run the games, run the Python scripts directly from the command line:

```bash
python3 <file_name>.py
