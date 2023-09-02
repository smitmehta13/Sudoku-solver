import random
from solver import solve


def generate_random_sudoku():
    # Create an empty 9x9 Sudoku board
    board = [[0 for _ in range(9)] for _ in range(9)]
    # Fill the Sudoku board with random values
    solve(board)
    # Randomly remove some values to make it a puzzle
    for _ in range(random.randint(30, 45)):  # Adjust the range for desired difficulty
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))

