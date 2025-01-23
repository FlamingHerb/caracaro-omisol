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
            # The minus 1 is necessary since Sudoku is one-indexed...
            # 1 = 1, 2 = 2, 3 = 4, 4 = 8, etc...
            pos = 1 << (sudoku_board[x][y] - 1)
            
            # Calculate what subgrid we are currently in.
            index = (x // 3) * 3 + y // 3
            
            # By comparing bits via bitmasking, we can check if a duplicate exists in a row,
            # column or grid.. We check first from row, to column, to subgrid. Really cool since
            # bitmasking is faster + space-saving vs. traditionally tracking it via lists, 
            # and then comparing it with `if x in list`.
            
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
    """Checks if the string of delimiters are balanced. Assumes string input are just delimiters."""
    
    # Delimiters for us to use (and their corresponding pairs)
    delimiters = {
        "(": ")",
        "[": "]",
        "{": "}",
    }
    
    # The stack to track our current progress.
    stack = []
    
    # We are now taking input, and we are assuming that we're only taking delimiters.
    inputString = input()
    
    # Traverse through input string
    for token in inputString:
        
        # IF it turns out that the delimiter we got is an open one.
        if token in delimiters:
            stack.append(token)
            
        # If its a closed delimiter. Equivalent to `elif token in delimiters.values():`
        else:
            # Case: If we get a closed delimiter on an empty stack, immediate print False.
            if len(stack) == 0:
                print("False")
                return
            
            # Case: If we pop a delimiter and see that its not paired with its supposed type, print false.
            # Also, really convenient way to just have it on one conditional as opposed to defining a new variable.
            if token != delimiters[stack.pop()]:
                print("False")
                return
            
    # Checks if there is still some stuff in the stack. Given we've reached the end, it's more likely to be
    # loose unpaired open delimiters.
    if len(stack) == 0:
        print("True")
    else:
        print("False")
    


if __name__ == "__main__":
    is_parenthesis_valid()