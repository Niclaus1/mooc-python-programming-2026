# Write your solution here

def copy_and_add(sudoku : list, row_no : int, column_no : int, number : int):
    new_sudoku = []
    
    for row in sudoku:
        new_sudoku.append(row[:])
        
    new_sudoku[row_no][column_no] = number    
    return new_sudoku

def print_sudoku(sudoku : list):

    for row in range(len(sudoku)):
        if row == 3 or row == 6:
            print('')
        for col in range(len(sudoku)):
            
            if col == 3 or col == 6:
                print(' ', end="")
                
            if sudoku[row][col] == 0:
                sudoku[row][col] = '_'
            print(sudoku[row][col], end=" ")
        print()

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)