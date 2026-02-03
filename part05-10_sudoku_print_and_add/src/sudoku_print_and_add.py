# Write your solution here

def add_number(sudoku : list, row_no : int, column_no : int, number : int):
    sudoku[row_no][column_no] = number

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
    s = [
    [ 9, '_', '_', 0, 8, '_', 3, '_', '_' ],
    [ 2, '_', '_', 2, 5, '_', 7, '_', '_' ],
    [ '_', 2, '_', 3, '_', '_', 0, '_', 4 ],
    [ 2, 9, 4, 0, '_', '_', 0, '_', '_' ],
    [ '_', '_', '_', 7, 3, '_', 5, 6, '_' ],
    [ 7, '_', 5, 0, 6, '_', 4, '_', '_' ],
    [ '_', '_', 7, 8, '_', 3, 9, '_', '_' ],
    [ '_', '_', 1, 0, '_', '_', 0, '_', 3 ],
    [ 3, '_', '_', 0, '_', '_', 0, '_', 2 ],
    ]
    print_sudoku(s)
    