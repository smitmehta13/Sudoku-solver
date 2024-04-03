from solver import solve
from generator import generate_random_sudoku, print_sudoku


def main():
    sudoku_board = generate_random_sudoku()
    print("Generated Sudoku Puzzle:")
    print_sudoku(sudoku_board)
    input("Press Enter to solve the puzzle...")
    solve(sudoku_board)
    print("Solved Sudoku Puzzle")
    print_sudoku(sudoku_board)

if __name__ == "__main__":
    main()