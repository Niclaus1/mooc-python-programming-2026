# Write your solution here
def column_correct(sudoku: list, column_no: int):

    col_count = []
    for row in range(len(sudoku)):
        col_count.append(sudoku[row][column_no])
    
    for duplicate in col_count:
        if duplicate > 0 and col_count.count(duplicate) > 1:
            return False
    return True
