def is_valid(board, row, col, num):
    """
    Check if 'num' is a valid candidate for the current position.

    Args:
        board (List[List[str]]): The Sudoku board.
        row (int): The row index.
        col (int): The column index.
        num (str): The number to check.

    Returns:
        bool: True if 'num' is a valid candidate, False otherwise.
    """
    # Check if 'num' is not in the current row, column and 3x3 sub-box
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False  # Return False if 'num' is already in the row or column
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False  # Return False if 'num' is already in the 3x3 sub-box
    return True  # Return True if 'num' is a valid candidate for the current position


def solve_sudoku(board):
    """
    Solve the Sudoku board using backtracking.

    Args:
        board (List[List[str]]): The Sudoku board.

    Returns:
        None
    """
    def solve():
        """
        Recursively solve the Sudoku board using backtracking.

        Returns:
            bool: True if the Sudoku board is solved, False otherwise.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # If the current position is empty
                    for num in '123456789':  # Try all possible numbers
                        if is_valid(board, row, col, num):  # If 'num' is valid candidate
                            board[row][col] = num  # Place 'num' in the current position
                            if solve():  # Recursively solve the Sudoku board
                                return True  # Return True if the Sudoku board is solved
                            board[row][col] = '.'  # If the current position is not the solution, backtrack
                    return False  # Return False if no valid candidate is found for the current position
        return True  # Return True if the Sudoku board is already solved

    solve()


# Example usage:
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solve_sudoku(board)
for row in board:
    print(row)  # Print the solved Sudoku board