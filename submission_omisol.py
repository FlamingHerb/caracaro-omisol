def is_sudoku_valid():
    """Checks if the current sudoku board is valid. Bottom-up approach(?) via bitmasking."""
    
    # Initialize Sudoku board.
    sudoku_board = [[0]*9]*9
    
    # Input, turn periods to 0s, and then add them per row via list comprehension.
    for i in range(0, 9):
        sudoku_board[i] = [int(x) for x in str(input()).replace(".", "0").split(" ")]
        #print(sudoku_board[i])

    # Used to track current progress and for immediate checking as opposed to constantly
    # checking the board all over again for each new cell traversed.
    rows    = [0]*9
    columns = [0]*9
    grids   = [0]*9
    
    # Start traversing.
    for x in range(0, 9):
        for y in range(0, 9):
            
            # Skip 0s.
            if sudoku_board[x][y] == 0: continue
            
            # Bitshift to correspond to proper placement in terms of binary.
            # 1 = 1, 2 = 2, 3 = 4, 4 = 8, etc...
            pos = 1 << (sudoku_board[x][y] - 1)
            
            # Calculate what subgrid we are currently in.
            index = (x // 3) * 3 + y // 3
            
            # By comparing bits via bitmasking, we can check if a duplicate exists in the rows.
            # We check first from row, to column, to subgrid. Really cool since bitmasking is faster
            # vs. traditionally tracking it via lists and then comparing it with `if x in list`.
            
            # Check if number already exists in the bit formation of a row via bitmasking.
            if (rows[x] & pos) > 0:
                print("False")
                return
            # Add the following to the row if it does not exist.
            else:
                rows[x] |= pos
                
            # Check if number already exists in the bit formation of a column via bitmasking.
            if (columns[y] & pos) > 0:
                print("False")
                return
            # Add the following to the column if it does not exist.
            else:
                columns[y] |= pos
            
            # Check if number already exists in the bit formation of a subgrid via bitmasking.
            if (grids[index] & pos) > 0:
                print("False")
                return
            # Add the following to the grid if it does not exist.
            else:
                grids[index] |= pos
    
    # Print true if there are no complication.
    print("True")
    return
    
def is_parenthesis_valid():
    return

if __name__ == "__main__":
    is_sudoku_valid()