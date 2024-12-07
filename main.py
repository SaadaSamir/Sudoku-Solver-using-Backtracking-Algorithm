import random

def is_valid(board, row, col, num):
    # Check if the number is not repeated in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is not repeated in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is not repeated in the 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    # Find the next empty spot (represented by 0)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try all possible numbers from 1 to 9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        # Recursively attempt to solve the rest of the board
                        if solve_sudoku(board):
                            return True
                        # Backtrack if no solution was found
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    return "\n".join(" ".join(str(cell) for cell in row) for row in board)

def generate_sudoku():
    # Create an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]

    # Fill the diagonal 3x3 subgrids to ensure valid solutions
    for i in range(0, 9, 3):
        nums = random.sample(range(1, 10), 9)
        for row in range(3):
            for col in range(3):
                board[i + row][i + col] = nums.pop()

    # Solve the puzzle using backtracking to ensure it's a valid Sudoku
    if solve_sudoku(board):
        return board
    else:
        return None

def create_unsolved_puzzle(board, empty_cells=40):
    # Randomly remove numbers from the solved board to create an unsolved puzzle
    unsolved_board = [row[:] for row in board]
    for _ in range(empty_cells):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        unsolved_board[row][col] = 0
    return unsolved_board

def save_sudoku_to_file(filename="sudoku_puzzles.txt"):
    with open(filename, "a") as file:
        board = generate_sudoku()
        if board:
            unsolved_board = create_unsolved_puzzle(board)
            
            file.write("Generated Sudoku Puzzle:\n")
            file.write(print_board(unsolved_board) + "\n\n")
            # Solve the puzzle
            solved_board = [row[:] for row in board]
            if solve_sudoku(solved_board):
                file.write("Solved Sudoku Puzzle:\n")
                file.write(print_board(solved_board) + "\n\n")
            else:
                file.write("No solution found.\n\n")

save_sudoku_to_file()
