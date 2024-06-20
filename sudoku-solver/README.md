# Sudoku Solver
* Write a function to solve a Sudoku puzzle by filling the empty cells. A Sudoku solution must satisfy all of the following rules:
    * Each of the digits 1-9 must occur exactly once in each row.
    * Each of the digits 1-9 must occur exactly once in each column.
    * Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

# Sudoku Solver
This project implements a Sudoku solver using backtracking. The solver takes an unsolved Sudoku board as input and fills in the empty cells with valid numbers to complete the board.

## Files

- `sudoku_solver.py`: Contains the main code for the Sudoku solver.

## Functions
### `is_valid(board, row, col, num)`
Checks if a number is a valid candidate for a specific position on the Sudoku board.

#### Arguments

- `board` (List[List[str]]): The Sudoku board.
- `row` (int): The row index.
- `col` (int): The column index.
- `num` (str): The number to check.

#### Returns

- `bool`: True if the number is a valid candidate, False otherwise.

#### Description

- Checks if the number is not present in the current row, column, and 3x3 sub-box.
- Returns False if the number is already present; otherwise, returns True.

### `solve_sudoku(board)`
Solves the Sudoku board using backtracking.

#### Arguments

- `board` (List[List[str]]): The Sudoku board.

#### Returns

- None

#### Description

- Defines a recursive function `solve` to solve the Sudoku board using backtracking.
- Iterates through each cell in the board and tries placing numbers from 1 to 9.
- Uses the `is_valid` function to check if the number is a valid candidate.
- Recursively solves the board by placing valid numbers and backtracks if a solution is not found.
- Solves the board in-place.

## Usage

- Import the `solve_sudoku` function from the `sudoku_solver.py` file.
- Provide a Sudoku board with empty cells represented by '.'.
- Call the `solve_sudoku` function with the board.
- The function will fill in the empty cells with valid numbers to solve the Sudoku.